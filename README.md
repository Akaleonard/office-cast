1. In Frontend, run npm install
2. run docker-compose build
3. run docker-compose up
4. connect to cli of the mongo container
    - Run mongo
    - run rs.initiate('rs0')
        - This creates the replica set - only needs to be done one time on the container