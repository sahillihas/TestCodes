// ----------- Minimum Movies ------------

int minimumMoves(const std::vector<int>& arr1, const std::vector<int>& arr2) {
    int total_moves = 0;
    for (size_t i = 0; i < arr1.size(); ++i) {
        std::string num1 = std::to_string(arr1[i]);
        std::string num2 = std::to_string(arr2[i]);
        for (size_t j = 0; j < num1.size(); ++j) {
            total_moves += std::abs(num1[j] - num2[j]);
        }
    }
    return total_moves;
}


// ---------- REST API ----------------

import requests

def getCapitalCity(country_name):
    # Construct the API endpoint with the country name
    url = f"https://jsonmock.hackerrank.com/api/countries?name={country_name}"
    
    # Make the GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()['data']
        
        # Check if the data array contains a country record
        if data:
            # Return the capital of the country
            return data[0]['capital']
        else:
            # Return '-1' if the country was not found
            return '-1'
    else:
        # Handle unexpected status codes
        return '-1'


// ------------ Big Companies -----------

SELECT C.NAME AS COMPANY_NAME
FROM COMPANY C
JOIN EMPLOYEE E ON C.ID = E.ID
JOIN SALARY S ON E.ID = S.EMPLOYEE_ID
GROUP BY C.NAME
HAVING AVG(S.SALARY) >= 40000;
// ---------- MCQs ------------------

4) Linked list as a queue, insertion O(1)
5) 3-arry tree, [2(n-1) + 3] = 13
6) Post order ABC = 5
7) i+=i => 256
8) find element in linkedlist => O(n)
9) Big O => upper bound on growth
10) (maybe D)
11) Pollution levels => 2
12) DQRWPMG (maybe)

// ------------- Knight Moves ----------

// initializing the matrix. 
int dp[8][8] = { 0 }; 
  
int getsteps(int x, int y,  
             int tx, int ty) 
{ 
    // if knight is on the target  
    // position return 0. 
    if (x == tx && y == ty) 
        return dp[0][0]; 
    else { 
          
        // if already calculated then return 
        // that value. Taking absolute difference. 
        if (dp[abs(x - tx)][abs(y - ty)] != 0) 
            return dp[abs(x - tx)][abs(y - ty)]; 
              
        else { 
  
            // there will be two distinct positions 
            // from the knight towards a target. 
            // if the target is in same row or column 
            // as of knight then there can be four 
            // positions towards the target but in that 
            // two would be the same and the other two 
            // would be the same. 
            int x1, y1, x2, y2; 
              
            // (x1, y1) and (x2, y2) are two positions. 
            // these can be different according to situation. 
            // From position of knight, the chess board can be 
            // divided into four blocks i.e.. N-E, E-S, S-W, W-N . 
            if (x <= tx) { 
                if (y <= ty) { 
                    x1 = x + 2; 
                    y1 = y + 1; 
                    x2 = x + 1; 
                    y2 = y + 2; 
                } else { 
                    x1 = x + 2; 
                    y1 = y - 1; 
                    x2 = x + 1; 
                    y2 = y - 2; 
                } 
            } else { 
                if (y <= ty) { 
                    x1 = x - 2; 
                    y1 = y + 1; 
                    x2 = x - 1; 
                    y2 = y + 2; 
                } else { 
                    x1 = x - 2; 
                    y1 = y - 1; 
                    x2 = x - 1; 
                    y2 = y - 2; 
                } 
            } 
              
            // ans will be, 1 + minimum of steps  
            // required from (x1, y1) and (x2, y2). 
            dp[abs(x - tx)][abs(y - ty)] =  
                           min(getsteps(x1, y1, tx, ty),  
                           getsteps(x2, y2, tx, ty)) + 1; 
                             
            // exchanging the coordinates x with y of both 
            // knight and target will result in same ans. 
            dp[abs(y - ty)][abs(x - tx)] =  
                           dp[abs(x - tx)][abs(y - ty)]; 
            return dp[abs(x - tx)][abs(y - ty)]; 
        } 
    } 
} 



  
