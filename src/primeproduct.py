def primeproduct(m):
     if (m > 0):
          count=0	
          for i in range(2,m):
               if m%i==0:
                    count+=1
          if count==2:
              return(True)
          else:
               return(False)
     else:
          return(False)
     
