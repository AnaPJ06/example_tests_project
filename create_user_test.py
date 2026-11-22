
import sender_stand_request
import data
def test_create_user_2_letter_in_first_name_get_success_response():
    # Guarda el cuerpo actualizado con el nombre "Aa"
    user_body = get_user_body("Aa")

    # Envía la solicitud para crear el usuario
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba que el código de estado sea 201
    assert user_response.status_code == 201

    # Comprueba que authToken exista y no esté vacío
    assert user_response.json()["authToken"] != ""

    # Consulta la tabla de usuarios
    users_table_response = sender_stand_request.get_users_table()

    # Construye el registro que esperamos encontrar en la tabla
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba que el usuario exista una sola vez
    assert users_table_response.text.count(str_user) == 1
