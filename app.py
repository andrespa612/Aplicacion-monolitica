from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas
tasks = []

# Ruta principal para mostrar la lista de tareas
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Ruta para agregar una nueva tarea
@app.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form['content']
    tasks.append(task_content)
    return redirect(url_for('index'))

# Ruta para eliminar una tarea
@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
