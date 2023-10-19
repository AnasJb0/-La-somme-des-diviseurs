M = int(input("Enter the first number (M): "))
N = int(input("Enter the second number (N): "))
SM = 0
for i in range(2, M): 
    if M % i == 0:
        SM = SM+i
SN = 0
for i in range(2, N):
    if N % i == 0:
        SN = SN+i
if SM == N and SN == M:
    print(M,"et",N,"are friends.")
else:
    print(M,"et",N,"are not friends.")