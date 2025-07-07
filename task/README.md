# Task


## API Endpoints

### 1. Retrieve a Single Task

- **URL:** `/api/tasks/1/`
- **Method:** `GET`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:**
    ```json
    {
      "id": 1,
      "title": "Design UI",
      "description": "Create wireframes for the dashboard",
      "status": "pending",
      "project": 1,
      "assignee": 2,
      "created_at": "2025-07-07T12:00:00Z"
    }
    ```

### 2. Update a Task

- **URL:** `/api/tasks/1/`
- **Method:** `PUT` or `PATCH`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Request Body:** (fields to update)
    ```json
    {
      "status": "completed"
    }
    ```
- **Response:** Updated task object

### 3. Delete a Task

- **URL:** `/api/tasks/1/`
- **Method:** `DELETE`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:** `204 No Content`


### 4. List All Comments for a Task

- **URL:** `/api/tasks/1/comments/`
- **Method:** `GET`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:**
    ```json
    [
      {
        "id": 1,
        "content": "Great work on this task!",
        "task": 1,
        "author": 2,
        "created_at": "2025-07-07T13:00:00Z"
      }
    ]
    ```

### 5. Create a New Comment for a Task

- **URL:** `/api/tasks/1/comments/`
- **Method:** `POST`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Request Body:**
    ```json
    {
      "content": "Please update the documentation."
    }
    ```
- **Response:**
    ```json
    {
      "id": 2,
      "content": "Please update the documentation.",
      "task": 1,
      "author": 2,
      "created_at": "2025-07-07T13:05:00Z"
    }
    ```

## Authentication

All endpoints require token authentication.  
Include your token in the `Authorization` header:

```
Authorization: Token <your_auth_token>
```

## Error Responses

- `400 Bad Request` – Invalid input
- `401 Unauthorized` – Authentication required
- `404 Not Found` – Task does not exist