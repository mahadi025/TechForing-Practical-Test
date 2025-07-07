# Comment

This app manages comments on tasks, including creation, listing, updating, and deletion.

## API Endpoints

### 1. Retrieve a Single Comment

- **URL:** `/api/comments/1/`
- **Method:** `GET`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:**
    ```json
    {
      "id": 1,
      "content": "Great work on this task!",
      "task": 1,
      "author": 2,
      "created_at": "2025-07-07T13:00:00Z"
    }
    ```

### 2. Update a Comment

- **URL:** `/api/comments/1/`
- **Method:** `PUT` or `PATCH`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Request Body:** (fields to update)
    ```json
    {
      "content": "Updated comment text."
    }
    ```
- **Response:** Updated comment object

### 3. Delete a Comment

- **URL:** `/api/comments/1/`
- **Method:** `DELETE`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:** `204 No Content`

## Authentication

All endpoints require token authentication.  
Include your token in the `Authorization` header:

```
Authorization: Token <your_auth_token>
```

## Error Responses

- `400 Bad Request` – Invalid input
- `401 Unauthorized` – Authentication required
- `404 Not Found` – Comment does not exist