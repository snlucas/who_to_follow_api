# Who To Follow API
Know who to follow based on their projects and stars.
If you started to learn some technology it's good to follow someone else that is actively creating projects using it.
This project want to make it easier.

### Endpoints
| Endpoint                           | Details                                                        | Method |
| ---------------------------------- | -------------------------------------------------------------- | ------ |
| /{technology}/projects             | Return the top 5 profile based on amount of projects           | GET    |
| /{technology}/stars                | Return the top 5 profile based on amount of stars              | GET    |
| /{technology}                      | Return the top 5 profile based on amount of projects and stars | GET    |
| /{technology}/.../{total_profiles} | Return a fixed number of profiles                              | GET    |
