from controller import Controller

def main():
    path = "sensor_2.data"
    #path = "sensor_readings_4.data"
    #path = "sensor_readings_test.data"
    #loadData(path)
    ctr = Controller()
    #ctr.gradient(path, 300, 0.005)
    ctr.evolutive(path, 300, 100)

if __name__ == '__main__':
    main()