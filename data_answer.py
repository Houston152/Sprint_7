

class ResponseMessages:
    COURIER_CREATED_SUCCESS = True
    DUPLICATE_COURIER_ERROR = "Этот логин уже используется. Попробуйте другой."
    MISSING_FIELDS_ERROR = "Недостаточно данных для создания учетной записи"
    AUTHORIZATION_MISSING_FIELDS_ERROR = "Недостаточно данных для входа"
    AUTHORIZATION_INVALID_CREDENTIALS_ERROR = "Учетная запись не найдена"
    AUTHORIZATION_SUCCESS = "id"
    ORDER_CREATED_SUCCESS = "track"
    ORDERS_LIST_SUCCESS = "orders"
