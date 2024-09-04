def aplica(x, h, w, v0, v1, k):
    # h0
    h[0] = sum(v0[i] * x[i] for i in range(len(v0)))
    
    # h1
    h[1] = sum(v1[i] * x[i] for i in range(len(v1)))
    
    # y output
    y = sum(w[i] * h[i] for i in range(len(w)))
    
    # Resetting h values
    h[0] = 0
    h[1] = 0
    
    return y * k

def treina(targ, train, x, h, w, v0, v1, k):
    taxaAprendizado = 0.28
    deltai = k * (targ - train)
    deltaj = k * (w[0] + w[1]) * deltai
    
    # Calculate deltaW
    deltaW = [deltai * (h[i] * k) for i in range(len(w))]
    
    # Calculate deltaV
    deltaV = [deltaj * x[i] for i in range(len(v0))]
    
    # Update w
    for i in range(len(w)):
        w[i] += taxaAprendizado * deltaW[i]
    
    # Update v0
    for i in range(len(v0)):
        v0[i] += taxaAprendizado * deltaV[i]
    
    # Update v1
    for i in range(len(v1)):
        v1[i] += taxaAprendizado * deltaV[i]
    
    # Resetting h values
    for i in range(len(h)):
        h[i] = 0

def printRNA(w, v0, v1):
    print("w:", w)
    print("v0:", v0)
    print("v1:", v1)

# Main function
if __name__ == "__main__":
    x = [1, 1, 1]
    h = [0, 0]
    w = [3, 1]
    v0 = [6, 3, 5]
    v1 = [2, 1, 3]
    k = 0.1
    
    # Input: mouth, eyebrows, and eyes
    
    targx = [3, 3, 3]  # Neutral
    print(aplica(targx, h, w, v0, v1, k))
    trainx = [4, 5.1, 3.2]
    print(aplica(trainx, h, w, v0, v1, k))
    
    printRNA(w, v0, v1)
    
    targ = aplica(targx, h, w, v0, v1, k)
    train = aplica(trainx, h, w, v0, v1, k)
    treina(targ, train, trainx, h, w, v0, v1, k)
    printRNA(w, v0, v1)
    print(aplica(trainx, h, w, v0, v1, k))
