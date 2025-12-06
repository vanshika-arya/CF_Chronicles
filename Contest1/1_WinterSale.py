X,P=map(int,input().split())
ans=P/(100-X)
original_P=ans*100
print(f"{original_P.__round__(2)}")