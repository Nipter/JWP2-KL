document.addEventListener('DOMContentLoaded', () => {
    const todoNameInput = document.getElementById('todo-name');
    const todoDescriptionInput = document.getElementById('todo-description');
    const addBtn = document.getElementById('add-btn');
    const todoList = document.getElementById('todo-list');
    const address = 'http://127.0.0.1:5000'

    function fetchTodos() {
        fetch(`${address}/get`)
            .then(response => response.json())
            .then(todos => {
                todoList.innerHTML = '';
                todos.forEach(todo => addTodoItem(todo.name, todo.description, todo.id));
            })
            .catch(error => console.error('Error fetching todos:', error));
    }

    fetchTodos();

    addBtn.addEventListener('click', () => {
        const name = todoNameInput.value.trim();
        const description = todoDescriptionInput.value.trim();

        if (name !== '') {
            fetch(`${address}/add`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, description })
            })
            .then(() => {
                fetchTodos();
            })
            .catch(error => console.error('Error adding todo:', error));
        }
    });

    function addTodoItem(name, description, id) {
        const li = document.createElement('li');
        const nameSpan = document.createElement('span');
        nameSpan.className = 'text';
        nameSpan.textContent = name;

        const descriptionSpan = document.createElement('span');
        descriptionSpan.className = 'description';
        descriptionSpan.textContent = description;

        const actionsDiv = document.createElement('div');
        actionsDiv.className = 'actions';

        const editBtn = document.createElement('button');
        editBtn.className = 'edit-btn';
        editBtn.textContent = 'Edytuj';

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'Usuń';

        actionsDiv.appendChild(editBtn);
        actionsDiv.appendChild(deleteBtn);

        li.appendChild(nameSpan);
        li.appendChild(descriptionSpan);
        li.appendChild(actionsDiv);
        todoList.appendChild(li);

        editBtn.addEventListener('click', () => {
            if (editBtn.textContent === 'Edytuj') {
                const nameInput = document.createElement('input');
                nameInput.type = 'text';
                nameInput.value = nameSpan.textContent;

                const descriptionTextarea = document.createElement('textarea');
                descriptionTextarea.value = descriptionSpan.textContent;

                li.insertBefore(nameInput, nameSpan);
                li.insertBefore(descriptionTextarea, descriptionSpan);
                li.removeChild(nameSpan);
                li.removeChild(descriptionSpan);
                editBtn.textContent = 'Zapisz';
            } else {
                const newName = li.querySelector('input').value;
                const newDescription = li.querySelector('textarea').value;

                fetch(`${address}/edit/${id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name: newName, description: newDescription })
                })
                .then(() => {
                    fetchTodos();
                })
                .catch(error => console.error('Error updating todo:', error));
            }
        });

        deleteBtn.addEventListener('click', () => {
            fetch(`${address}/delete/${id}`, {
                method: 'DELETE'
            })
            .then(() => {
                fetchTodos();
            })
            .catch(error => console.error('Error deleting todo:', error));
        });
    }
});
