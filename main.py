from controller import loadData

def main():
    #path = "sensor_readings_2.data"
    #path = "sensor_readings_4.data"
    path = "sensor_readings_24.data"

    loadData(path)
    print("main")

if __name__ == '__main__':
    main()