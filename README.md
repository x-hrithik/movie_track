# Palace REST API

A Flask based REST API for tracking movies and sharing movie collections with friends. This API is used for managing movie search lists based on TMDB's API and social interactions. 

## Overview

Palace API provides endpoints for:

- **User Authentication** – JWT based authentication with nickname based signup/login (will be later changed to use Discord authentication)
- **Movie Search** – Search movies via TMDB API
- **Watchlists** – Create and manage personal movie lists
- **Movie Management** – Add or remove movies to or from lists with TMDB metadata
- **Clubs** – Create or join movie clubs to share and collaborate on movie lists with other users

## Tech Stack
- **Framework**: Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-JWT-Extended
- **External API**: TMDB (The Movie Database)
- **CORS**: Enabled for cross origin requests (useful for using React)

## Setup & Installation

### Prerequisites

- Python 3.7+
- TMDB API key (get one free at [https://www.themoviedb.org]

### 1. Clone the Repository

### 2. Create Virtual Environment

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

### 4. Run the Application

```bash
python backend/app.py
```

The API will start at `http://localhost:5000`

## Future Ideas

- Discord OAuth integration 
- Production database (PostgreSQL/MySQL)
- Rate limiting
- Movie ratings and reviews
- Live watch party
- Friends List
- Notification system
