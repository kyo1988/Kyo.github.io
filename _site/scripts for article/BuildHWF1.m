% matlab2016b
function[Q,r,pu,pm,pd,d,m,N,k]=BuildHWF1(a,sigma,t,P) 

[N,~]=size(P);
deltaX=zeros(N,1); 
x=zeros(2*N+1,N+1); 
r=zeros(2*N+1,N+1); 
pu=zeros(2*N+1,N+1); 
pm=zeros(2*N+1,N+1); 
pd=zeros(2*N+1,N+1); 
Q=zeros(2*N+1,N+1);
d=zeros(2*N+1,N+1);
g=zeros(N,1); 
k=zeros(2*N+1,N+1); 
Q(N+1,1)=1; 
m=zeros(N,1); 
m(1)=0; 
m(2)=1; 

for i=1:N-1 
    deltaX(i+1)=sigma*sqrt(3.*(t(i+1)-t(i)));
end

for i=1:N-1 
    for j=m(i):-1:-m(i) 
        M=-j.*deltaX(i).*a*(t(i+1)-t(i));
        V=sigma.^2.*(t(i+1)-t(i ));

        k(N+1-j, i)=round((j.*deltaX(i)+M)./deltaX(i+1)); 
        
        alpha=(j.*deltaX(i)+M-k(N+1-j, i).*deltaX(i+1))./deltaX(i+1);

        pu(N+1-j, i)=V./(2.*deltaX(i+1).^2)+(alpha.^2+alpha)./2;
        pd(N+1-j, i)=V./(2.*deltaX(i+1).^2)+(alpha.^2-alpha)./2; 
        pm(N+1-j, i)=1-V./(deltaX(i+1).^2)-alpha.^2;
        
    if j==max(m(i)) 
        m(i+1)=k(N+1-j,i)+1; 
    end
    
    end
end

    for i=1:N-1
        for j=1:m(i)
            x(N+1+j, i)=x(N+1+j-1, i)-deltaX(i); 
            x(N+1-j, i)=x(N+1-j+1, i)+deltaX(i); 
        end
    end  

    for i=1:N-1 
        if i==2
            Q(N+2, i)=Q(N+1, i-1).*pu(N+1, i-1).*exp(-r(N+1, i-1).*(t(i)-t(i-1))); 
            Q(N+1, i)=Q(N+1, i-1).*pm(N+1, i-1).*exp(-r(N+1, i-1).*(t(i)-t(i-1))); 
            Q(N, i)=Q(N+1, i-1).*pd(N+1, i-1).*exp(-r(N+1, i-1).*(t(i)-t(i-1))); 
        elseif i>=3
            for j=m(i):-1:-m( i ) 
                for jj=m(i-1):-1:-m(i-1) 
                    Q(N+1+j, i)=Q(N+1+j, i)...
                    +Q(N+1+jj, i-1).*pu(N+1+jj, i-1).*exp(-r(N+1+jj, i-1).*(t(i)-t(i-1))).*(k(N+1+jj,i-1)+1==j)...
                    +Q(N+1+jj, i-1).*pm(N+1+jj, i-1).*exp(-r(N+1+jj, i-1).*(t(i)-t(i-1))).*(k(N+1+jj,i-1)==j)...
                    +Q(N+1+jj, i-1).*pd(N+1+jj, i-1).*exp(-r(N+1+jj, i-1).*(t(i)-t(i-1))).*(k(N+1+jj,i-1)-1==j);
                end 
            end 
        end

    if i==1
        g(i)=-log(P(i+1))./(t(i+1)-t(i)); 
    elseif i>=2 
        sum=0; 
        for j=m(i) :-1 :-m(i) 
            sum=sum+Q(N+1+j, i).*exp(-x(N+1+j, i).*(t(i+1)-t(i))); 
        end 
            g(i)=(log(sum)-log(P(i+1)))./(t(i+1)-t(i)); 
    end

        for j=m(i):-1:-m(i)
            r(N+1-j, i)=x(N+1-j, i)+g(i); 
            d(N+1-j, i)=exp(-r(N+1-j, i).*(t(i+1)-t(i))); 
        end 
    end
end