    

  Small project test of IMDB site, that includes testing of:
   - sign in process validation
   - add movie from 'coming soon' list verification
   - save the first movie in the list and validate the same movie name added in my watch list after sign in
   - delete movie from my watchlist verification
   - list changed verification


Prerequisites:

    1. Required version of Python : 3.8.2 and above
    2. install selenium `pip install selenium`
    3. install pytest `pip install pytest`
    4. install chrome `pip install webdriver-manager`

Project structure:

    - The files divided to Page Object moduls (heaader, sign in page,coming soon page,my watch list)
    - Configuration file (for URL, user, password)
    - Test cases to run with pytest

TO RUN PYTEST FROM TERMINAL:
    1. CD to TestCases

    2. pytest -v -s .\test_select_add_watchlist.py ( aftre .\ need to select with tab witch 
    test to run ,ex. )


NOTE  -  if in the first run the test fails or the app page is stuck, that is because this webpage 
        has dynamic elements, and I have the implicitly_wait method in all my Tests classes
        which waits for all elements to load. The solution is to terminate the first run 
        and run again

        
