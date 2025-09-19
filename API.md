### Curator 
#### Get all curators
endpoint: /api/curator  
method: GET
Response: "List[Curator]"

#### Get curator by id
endpoint: /api/curator/{id}
method: GET

#### Create curator
endpoint: /api/curator
method: POST

#### Update curator
endpoint: /api/curator/{id}
method: PUT

#### Delete curator
endpoint: /api/curator/{id}
method: DELETE

### PlayerTeam
#### Get all player teams
endpoint: /api/playerteam
method: GET

#### Get player team by id
endpoint: /api/playerteam/{id}
method: GET

#### Create player team
endpoint: /api/playerteam
method: POST

#### Update player team
endpoint: /api/playerteam/{id}
method: PUT

#### Delete player team
endpoint: /api/playerteam/{id}
method: DELETE

#### Add score to player team
endpoint: /api/playerteam/{id}/add_score
method: POST
Request:
    query id:int
    json: {
        "score": int
    }
Response:{
    score:int
    current_station:int

}


#### Get top 3 player teams by score
endpoint: /api/playerteam/get_top_3/
method: GET

#### Set current station
endpoint: /api/playerteam/{id}/set_current_station
method: POST

### Station
#### Get all stations
endpoint: /api/station
method: GET

#### Get station by id
endpoint: /api/station/{id}
method: GET

#### Create station
endpoint: /api/station
method: POST

#### Update station 
endpoint: /api/station/{id}
method: PUT

#### Delete station
endpoint: /api/station/{id}
method: DELETE

#### StationOrder 
##### Get all station orders
endpoint: /api/stationorder
method: GET

##### Get station order by id
endpoint: /api/stationorder/{id}
method: GET

##### Create station order
endpoint: /api/stationorder
method: POST

##### Update station order
endpoint: /api/stationorder/{id}
method: PUT

##### Delete station order
endpoint: /api/stationorder/{id}
method: DELETE

### Task
#### Get all tasks
endpoint: /api/task
method: GET

#### Get task by id
endpoint: /api/task/{id}
method: GET

#### Create task
endpoint: /api/task
method: POST

#### Update task
endpoint: /api/task/{id}
method: PUT

#### Delete task
endpoint: /api/task/{id}
method: DELETE

### Token
#### Get JWT
endpoint: /api/token
method: POST
Response: {
    "access": str
    "refresh":str
}

#### Refresh JWT
endpoint: /api/token/refresh
method: POST
Request: Headers{
    Authorizated Bearer "refresh_token"
}
Response: {
    "access": str
}
#### Verify JWT
endpoint: /api/token/verify
method: POST
Request: Headers{
    Authorizated Bearer "access_token"
}
Response: {
    "details": str
}
