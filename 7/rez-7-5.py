K1, M, K2, P2, N2 = map(int, input().split())
if M*P2-N2 > K2:
    print(-1,-1)
else:
    avgK = (K2+(N2 + (M * (P2 - 1)))-1) // (N2 + (M * (P2 - 1)))
    P1 = (K1 + (M * avgK) - 1) // (M * avgK)
    N1 = ((K1 - (M * avgK)*(P1-1)) + avgK - 1) // avgK
    print(P1,N1)