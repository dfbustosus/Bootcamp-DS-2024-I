gather_user_data = {
    "name": "gather_user_data",
    "description": "Obtener datos del usuario para hacer una reserva en el restaurante Condorito",
    "parameters": {
        "type": "object",
        "properties": {
            "telefono": {"type": "string", "description": "Un telefono valido, e.g., 3362296959"},
            "nombre": {"type": "string", "description": "Primer nombre del usuario, e.g., David"},
            "apellido": {"type": "string", "description": "Apellido del usuario, e.g., Bustos"},
            "email": {"type": "string", "description": "Un email valido, e.g., david@gmail.com"},
        },
        "required": ["telefono", "nombre", "apellido", "email"]
    }
}

gather_reservation_data = {
    "name": "gather_reservation_data",
    "description": "Obtener los datos para la reserva en el restaurante Condorito",
    "parameters": {
        "type": "object",
        "properties": {
            "fecha": {"type": "string", "description": "Fecha deseada de visita, e.g., Nov 11 2023"},
            "hora": {"type": "string", "description": "Hora deseada de visita, e.g., 4PM"}
        },
        "required": ["fecha", "hora"]
    }
}

not_talk = {
    "name": "not_talk",
    "description": "Preguntarle al usuario si quiere continuar hablando, si no desea terminar la ayuda del asistente",
    "parameters": {
        "type": "object",
        "properties": {
            "fin": {"type": "boolean", "description": "El usuario no quiere hablar mas"}
        },
        "required": ["fin"]
    }
}