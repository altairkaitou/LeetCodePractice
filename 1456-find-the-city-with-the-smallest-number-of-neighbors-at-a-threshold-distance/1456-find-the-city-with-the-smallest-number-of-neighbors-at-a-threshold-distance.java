class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] graph_dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(graph_dist[i], Integer.MAX_VALUE / 2);
            graph_dist[i][i] = 0;   
        }

        for (int[] edge : edges) {
            int fromDes = edge[0];
            int toDes = edge[1];
            int weightDes = edge[2];
            graph_dist[fromDes][toDes] = weightDes;
            graph_dist[toDes][fromDes] = weightDes;
        }


        // Floyd-Warshall Algorithm
        for(int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (graph_dist[i][j] > graph_dist[i][k] + graph_dist[k][j]) {
                        graph_dist[i][j] = graph_dist[i][k] + graph_dist[k][j];

                    }
                }
            }
        }

        int minCount = Integer.MAX_VALUE;
        int CityMin = -1;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && graph_dist[i][j] <= distanceThreshold) {
                    count++;
                }
            }

            if(count < minCount || count == minCount && i > CityMin) {
                    CityMin = i;
                    minCount = count;
            }
        }
        return CityMin; 
        
    }
}