#include <stdio.h>

#define MAX 20

struct Edge {
int u, v, w;
};

int parent[MAX];

int find(int i) {
while (parent[i] != i)
i = parent[i];
return i;
}

void unionSet(int i, int j) {
int a = find(i);
int b = find(j);
parent[a] = b;
}

void sortEdges(struct Edge edges[], int e) {
int i, j;
struct Edge temp;
for (i = 0; i < e - 1; i++) {
for (j = 0; j < e - i - 1; j++) {
if (edges[j].w > edges[j + 1].w) {
temp = edges[j];
edges[j] = edges[j + 1];
edges[j + 1] = temp;
}
}
}
}

int main() {
int n, e, i, count = 0, minCost = 0;
struct Edge edges[MAX], result[MAX];

printf("Enter number of vertices: ");
scanf("%d", &n);

printf("Enter number of edges: ");
scanf("%d", &e);

printf("Enter edges (u v weight):\n");
for (i = 0; i < e; i++) {
scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].w);
}

for (i = 0; i < n; i++)
parent[i] = i;

sortEdges(edges, e);

for (i = 0; i < e && count < n - 1; i++) {
int uRoot = find(edges[i].u);
int vRoot = find(edges[i].v);

if (uRoot != vRoot) {
result[count++] = edges[i];
minCost += edges[i].w;
unionSet(uRoot, vRoot);
}
}

printf("\nEdges in Minimum Spanning Tree:\n");
for (i = 0; i < count; i++) {
printf("%d -- %d == %d\n", result[i].u, result[i].v, result[i].w);
}

printf("Minimum Cost = %d\n", minCost);

return 0;
}
