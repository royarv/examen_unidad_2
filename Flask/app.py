"""
Examen Unidad III 
Autor: Rodrigo Arvizu Medina
Fecha: 29/10/25

Descripción:
Objetivo del examen
Desarrollar una API básica con Flask que permita:

Crear un diccionario de dispositivos de red.
Agregar nuevos dispositivos.
Modificar dispositivos existentes.
Mostrar un listado de todos los dispositivos en formato HTML, 
donde cada dispositivo se muestre en un <div> con nombre, 
descripción y características

Requisitos técnicos

Usar Flask.
Usar un diccionario como estructura principal de almacenamiento.
Implementar al menos tres rutas:

GET /dispositivos_html: muestra todos los dispositivos en HTML.
POST /dispositivos: agrega un nuevo dispositivo.
PUT /dispositivos/<id>: modifica un dispositivo existente.

Ejemplo del Diccionario de dispositivos: 
{
  "id": "router01",
  "nombre": "Router Principal",
  "descripcion": "Router de borde para salida a Internet",
  "ip": "192.168.1.1",
  "mac": "00:1A:2B:3C:4D:5E",
  "ubicacion": "Sala de servidores",
  "tipo": "Router",
  "otros": ""
}

Recuerda tener al menos 3 commits en tu repositorio. 

Para puntos extra
Puedes ocupar css para añadir puntos a tu examen, perzonalizalo con estilos como el siguiente:
<style>
    .dispositivo {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px;
    }
</style>

Puntos extra para añador formula en el cmapo de otros
la formula es la siguente: 

último octeto de la IP * 3 + longitud del nombre del dispositivo + ":" + nombre (Cambiando los espacios por _)

"""
from flask import Flask, render_template_string, request,redirect, url_for

app = Flask(__name__)

datos_acumulados = []

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    
    id = None
    nombre = None
    descripcion = None
    ip = None
    mac = None
    ubicacion = None
    tipo = None
    otros = None

    
    if request.method == 'POST':
       
        id = request.form['id']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        ip = request.form['ip']
        mac = request.form['mac']
        ubicacion = request.form['ubicacion']
        tipo = request.form['tipo']
        otros = request.form['otros']
        
    
        datos_acumulados.append({
            'id': id,
            'nombre': nombre,
            'descripcion': descripcion,
            'ip': ip,
            'mac': mac,
            'ubicacion': ubicacion,
            'tipo': tipo,
            'otros': otros
        })

    
    html = f"""
    <html>
    <body>
        <h2>Agregar Dispositivos</h2>
        <form method="POST">
            <input type="text" name="id" placeholder="ID" value="{id or ''}"><br>
            <input type="text" name="nombre" placeholder="Nombre" value="{nombre or ''}"><br>
            <input type="text" name="descripcion" placeholder="Descripcion" value="{descripcion or ''}"><br>
            <input type="text" name="ip" placeholder="IP" value="{ip or ''}"><br>
            <input type="text" name="mac" placeholder="MAC" value="{mac or ''}"><br>
            <input type="text" name="ubicacion" placeholder="Ubicacion" value="{ubicacion or ''}"><br>
            <input type="text" name="tipo" placeholder="Tipo" value="{tipo or ''}"><br>
            <input type="text" name="otros" placeholder="Otros" value="{otros or ''}"><br>
            <button type="submit">Enviar</button>
            
        </form>

        <h3>Lista de Dispositivos</h3>
        <ul>
    """
    
    for entry in datos_acumulados:
        html += f"""
            <li>
                <strong>ID:</strong> {entry['id']}<br>
                <strong>Nombre:</strong> {entry['nombre']}<br>
                <strong>Descripción:</strong> {entry['descripcion']}<br>
                <strong>IP:</strong> {entry['ip']}<br>
                <strong>MAC:</strong> {entry['mac']}<br>
                <strong>Ubicación:</strong> {entry['ubicacion']}<br>
                <strong>Tipo:</strong> {entry['tipo']}<br>
                <strong>Otros:</strong> {entry['otros']}<br>
                <hr>
                <form action="/test2/actualizar/{entry['id']}" method="GET">
                    <button type="submit">Actualizar</button>
                </form>
            </li>
        """
    
    html += """
        </ul>
    </body>
    </html>
    """

    return render_template_string(html)
@app.route('/test2/actualizar/<device_id>', methods=['GET', 'POST'])
def actualizar(device_id):
    dispositivo = next((d for d in datos_acumulados if d['id'] == device_id), None)

    if not dispositivo:
        return redirect(url_for('test2'))

    
    if request.method == 'POST':
        dispositivo['id'] = request.form['id']
        dispositivo['nombre'] = request.form['nombre']
        dispositivo['descripcion'] = request.form['descripcion']
        dispositivo['ip'] = request.form['ip']
        dispositivo['mac'] = request.form['mac']
        dispositivo['ubicacion'] = request.form['ubicacion']
        dispositivo['tipo'] = request.form['tipo']
        dispositivo['otros'] = request.form['otros']

        
        return redirect(url_for('test2'))

    html = f"""
    <html>
    <body>
        <h2>Actualizar Dispositivo</h2>
        <form method="POST">
            <input type="text" name="id" placeholder="ID" value="{dispositivo['id']}" readonly><br>
            <input type="text" name="nombre" placeholder="Nombre" value="{dispositivo['nombre']}"><br>
            <input type="text" name="descripcion" placeholder="Descripcion" value="{dispositivo['descripcion']}"><br>
            <input type="text" name="ip" placeholder="IP" value="{dispositivo['ip']}"><br>
            <input type="text" name="mac" placeholder="MAC" value="{dispositivo['mac']}"><br>
            <input type="text" name="ubicacion" placeholder="Ubicacion" value="{dispositivo['ubicacion']}"><br>
            <input type="text" name="tipo" placeholder="Tipo" value="{dispositivo['tipo']}"><br>
            <input type="text" name="otros" placeholder="Otros" value="{dispositivo['otros']}"><br>
            <button type="submit">Actualizar Dispositivo</button>
        </form>
        <br>
        <a href="/test2">Volver a la pagina principal</a>
    </body>
    </html>
    """

    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True)






   

