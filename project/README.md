# Projects

## API Endpoints

### 1. List All Projects

- **URL:** `/api/projects/`
- **Method:** `GET`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Project Alpha",
        "description": "First project",
        "created_at": "2025-07-07T12:00:00Z",
        "owner": 2
      },
      ...
    ]
    ```

### 2. Create a New Project

- **URL:** `/api/projects/`
- **Method:** `POST`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Request Body:**
    ```json
    {
      "name": "Project Beta",
      "description": "Second project"
    }
    ```
- **Response:**
    ```json
    {
      "id": 2,
      "name": "Project Beta",
      "description": "Second project",
      "created_at": "2025-07-07T12:10:00Z",
      "owner": 2
    }
    ```

### 3. Retrieve a Single Project

- **URL:** `/api/projects/{id}/`
- **Method:** `GET`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:**
    ```json
    {
      "id": 1,
      "name": "Project Alpha",
      "description": "First project",
      "created_at": "2025-07-07T12:00:00Z",
      "owner": 2
    }
    ```

### 4. Update a Project

- **URL:** `/api/projects/{id}/`
- **Method:** `PUT` or `PATCH`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Request Body:** (fields to update)
    ```json
    {
      "description": "Updated description"
    }
    ```
- **Response:** Updated project object

### 5. Delete a Project

- **URL:** `/api/projects/{id}/`
- **Method:** `DELETE`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:** `204 No Content`


### 6. List All Tasks for a Project

- **URL:** `/api/projects/1/tasks/`
- **Method:** `GET`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Response:**
    ```json
    [
      {
        "id": 1,
        "title": "Design UI",
        "description": "Create wireframes for the dashboard",
        "status": "pending",
        "project": 1,
        "assignee": 2,
        "created_at": "2025-07-07T12:00:00Z"
      },
    ]
    ```

### 7. Create a New Task for a Project

- **URL:** `/api/projects/1/tasks/`
- **Method:** `POST`
- **Headers:**  
  `Authorization: Token <your_auth_token>`
- **Request Body:**
    ```json
    {
      "title": "Develop API",
      "description": "Implement authentication endpoints",
      "status": "in_progress",
      "project": 1,
      "assignee": 2
    }
    ```
- **Response:**
    ```json
    {
      "id": 2,
      "title": "Develop API",
      "description": "Implement authentication endpoints",
      "status": "in_progress",
      "project": 1,
      "assignee": 2,
      "created_at": "2025-07-07T12:30:00Z"
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
- `404 Not Found` – Project does not exist