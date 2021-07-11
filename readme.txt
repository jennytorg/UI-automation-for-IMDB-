    
    
    PROJECT :
    IMDB movies site, small project include testing of validate sign in process
    add movie from 'coming soon' list, save the first movie in the list and validte
    the same movie name added in my watch list after sign in. verify delete movie 
    from my watch list, and verify the list changed



    Rrequired version of Python : 3.8.2
    

    TO RUN PYTEST FROM TERMINAL:
    1. CD to TestCases

    2. pytest -v -s .\test_delete_movie_from_watchlist.py ( aftre .\ need to select with tab witch 
    test to run ,ex. )


NOTE  - if in the first run the test is failed or the app page stuck, that is because this webpage 
        has dynamic elements, and I have the implicitly_wait method in all my Tests classes
        witch waits to all elenemts to load, the solution is to terminate the first run 
        and run again

        
