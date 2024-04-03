import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Sorting Animation")
screen.setup(width=800, height=600)
screen.bgcolor('white')

# Function to draw a bar
def draw_bar(t, height, x):
    t.penup()
    t.goto(x, -250)
    t.pendown()
    t.setheading(90)
    t.forward(height)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(height)

# Function to create random data
def create_data():
    data = [random.randint(10, 200) for _ in range(10)]
    return data

# Function to draw bars
def draw_data(t, data):
    t.clear()
    t.speed(0)
    t.penup()
    for i, height in enumerate(data):
        draw_bar(t, height, -350 + i * 80)

# Function to swap two elements in the data list
def swap(data, i, j):
    data[i], data[j] = data[j], data[i]

# Bubble sort
def bubble_sort(data, t):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                swap(data, j, j+1)
                t.clear()
                draw_data(t, data)
                t.penup()
                t.goto(-350 + j * 80, -250)
                t.dot(50, 'red')
                t.goto(-350 + (j+1) * 80, -250)
                t.dot(50, 'red')
                time.sleep(0.2)
                t.penup()
                t.goto(-350 + j * 80, -250)
                t.dot(50, 'white')
                t.goto(-350 + (j+1) * 80, -250)
                t.dot(50, 'white')

# Insertion sort
def insertion_sort(data, t):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j] :
            data[j+1] = data[j]
            j -= 1
            t.clear()
            draw_data(t, data)
            t.penup()
            t.goto(-350 + (j+1) * 80, -250)
            t.dot(50, 'red')
            t.goto(-350 + (j+2) * 80, -250)
            t.dot(50, 'red')
            time.sleep(0.2)
            t.penup()
            t.goto(-350 + (j+1) * 80, -250)
            t.dot(50, 'white')
            t.goto(-350 + (j+2) * 80, -250)
            t.dot(50, 'white')
        data[j+1] = key

# Selection sort
def selection_sort(data, t):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        swap(data, i, min_idx)
        t.clear()
        draw_data(t, data)
        t.penup()
        t.goto(-350 + i * 80, -250)
        t.dot(50, 'red')
        t.goto(-350 + min_idx * 80, -250)
        t.dot(50, 'red')
        time.sleep(0.2)
        t.penup()
        t.goto(-350 + i * 80, -250)
        t.dot(50, 'white')
        t.goto(-350 + min_idx * 80, -250)
        t.dot(50, 'white')

# Quick sort
def quick_sort(data, t, low, high):
    if low < high:
        pi = partition(data, t, low, high)
        quick_sort(data, t, low, pi-1)
        quick_sort(data, t, pi+1, high)

def partition(data, t, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            swap(data, i, j)
            t.clear()
            draw_data(t, data)
            t.penup()
            t.goto(-350 + i * 80, -250)
            t.dot(50, 'red')
            t.goto(-350 + j * 80, -250)
            t.dot(50, 'red')
            time.sleep(0.2)
            t.penup()
            t.goto(-350 + i * 80, -250)
            t.dot(50, 'white')
            t.goto(-350 + j * 80, -250)
            t.dot(50, 'white')
    swap(data, i+1, high)
    return i+1

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.color('black')
    t.fillcolor('lightblue')

    algorithms = {
        'bubble': bubble_sort,
        'insertion': insertion_sort,
        'selection': selection_sort,
        'quick': quick_sort
    }

    # Let user choose sorting algorithm
    print("Choose a sorting algorithm:")
    for idx, algorithm in enumerate(algorithms.keys(), 1):
        print(f"{idx}. {algorithm.capitalize()} Sort")

    choice = input("Enter the number of your choice: ")

    try:
        choice = int(choice)
        algorithm = list(algorithms.keys())[choice - 1]
        if algorithm in algorithms:
            data = create_data()
            draw_data(t, data)
            algorithms[algorithm](data[:], t)
        else:
            print("Invalid choice. Please enter a number between 1 and", len(algorithms))
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

    screen.mainloop()

if __name__ == "__main__":
    main()
