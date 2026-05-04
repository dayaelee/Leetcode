import java.util.*;
import java.io.*;

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        int[][] outputt = new int[n][n];
        for(int i = 0; i<n ; i++){
            for(int j = 0; j<n ; j++){
                int y = i;
                int x = j;

                int ny = x;
                int nx = n-y-1;

                int tmp = matrix[y][x];
                outputt[ny][nx]=tmp;
            }
        }

        for(int i = 0; i<n; i++){
            for(int j  = 0; j<n; j++){
                matrix[i][j] = outputt[i][j];
            }
        }

        /**
        
        0,0   0,1   0,2
        1,0   1,1   1,2
        2,0   2,1   2,2

        y, x         x, abs(n-y)   
        0,0 -> 0,2         
        0,1 -> 1,2
        0,2 -> 2,2

        1,0 ->0,1
        1,1 ->1,1
        1,2 ->2,1

        2,0 ->0,0
        2,1 ->1,0
        2,2 ->2,0
        
        
        0,0   0,1   0,2   0,3
        1,0   1,1   1,2   1,3
        2,0   2,1   2,2   2,3
        3,0   3,1   3,2   3,3
        
        y, x         x, abs(n-y)   
        0,0 -> 0,3
        0,1 -> 1,3
        0,2 -> 2,3
        0,3 -> 3,3

        1,0 -> 0,2
        1,1 -> 1,2
        1,2 -> 2,2
        1,3 -> 3,2

        2,0 -> 0,1
        2,1 -> 1,1
        2,2 -> 2,1
        2,3 -> 3,1

        3,0 -> 0,0
        3,1 -> 1,0
        3,2 -> 2,0
        3,3 -> 3,0
        
         */
    }
}