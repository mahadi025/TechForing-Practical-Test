# User

## API Endpoints

### 1. Register a New User

- **URL:** `/api/users/register/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "username": "newuser",
      "password": "yourpassword",
      "email": "user@example.com"
    }
    ```
- **Response:**
    ```json
    {
      "id": 2,
      "username": "newuser",
      "email": "user@example.com"
    }
    ```

### 2. Obtain Auth Token (Login)

- **URL:** `/api/users/login/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "username": "newuser",
      "password": "yourpassword"
    }
    ```
- **Response:**
    ```json
    {
      "token": "your_auth_token"
    }
    ```

### 3. Get User Profile

- **URL:** `/api/users/2`
- **Method:** `GET`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:**
    ```json
    {
      "id": 2,
      "username": "newuser",
      "email": "user@example.com"
    }
    ```

### 4. Update User

- **URL:** `/api/users/1`
- **Method:** `PUT` or `PATCH`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Request Body:** (fields to update)
    ```json
    {
      "email": "newemail@example.com"
    }
    ```
- **Response:** Updated user object

### 5. Delete User

- **URL:** `/api/users/{id}/`
- **Method:** `DELETE`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:** `204 No Content`

## Authentication

Most endpoints require token authentication.  
Include your token in the `Authorization` header:

```
Authorization: Token <your_auth_token>
```

## Error Responses

- `400 Bad Request` – Invalid input
- `401 Unauthorized` – Authentication required
- `404 Not Found` – Resource does not exist