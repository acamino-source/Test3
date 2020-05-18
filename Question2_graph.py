from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def divide(list):
    x = []
    y = []
    z = []
    for point in list:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    return x, y, z

if __name__ == "__main__":
    start = [[38.34414, 82.00822, 9.77062], [31.06418, 30.17703, 10.37498], [7.27996, 51.83119, 12.98979], [69.40832, 12.18525, 14.96979], [7.75246, 94.19347, 9.50209], [77.16078, 6.37872, 12.8852], [84.91325, 0.57218, 7.22021], [62.07403, 6.9509, 9.3871], [46.98728, 7.52308, 10.7523]]
    optimized = [[38.34414, 82.00822, 9.77062], [7.75246, 94.19347, 9.50209], [7.27996, 51.83119, 12.98979], [31.06418, 30.17703, 10.37498], [62.07403, 6.9509, 9.3871], [46.98728, 7.52308, 10.7523], [69.40832, 12.18525, 14.96979], [77.16078, 6.37872, 12.8852], [84.91325, 0.57218, 7.22021]]
    x,y,z = divide(start)
    a,b,c = divide(optimized)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # starting path
    # ax.plot(x, y, z,c='r')

    # optimized path
    ax.plot(a,b,c,c='b')

    plt.show()
