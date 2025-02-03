from exo1.utils import binary_search
from exo2.utils import Graph, bfs, dfs_iterative, dfs_recursive, shortest_path_bfs
from exo3.utils import knapsack
from exo4.utils import merge_intervals
from exo5.utils import max_subarray_sum

def main():
    exercises = {
        "1": "Binary Search",
        "2": "Graph Traversal (BFS)",
        "3": "Knapsack Problem",
        "4": "Merge Intervals",
        "5": "Maximum Subarray Sum"
    }
    
    while True:
        print("\nSelect an exercise:")
        for key, value in exercises.items():
            print(f"{key}. {value}")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "6":
            print("Exiting...")
            break
        
        if choice not in exercises:
            print("Invalid choice. Try again.")
            continue
        
        print(f"You selected: {exercises[choice]}")
        mode = input("Do you want to use default test (Y/N)? ").strip().lower()
        
        if choice == "1":  # Binary Search
            if mode == "y":
                # Example of sorted lists  and targets to find
                sorted_lists = [
                    ([1, 3, 5, 7, 9, 11, 13], 7),    # Target in the list
                    ([2, 4, 6, 8, 10, 12], 5),       # absent in the list 
                    ([0, 1, 2, 3, 4, 5, 6], 0),      # First element
                    ([10, 20, 30, 40, 50], 50),      # last element
                ]

                for arr, target in sorted_lists:
                    result = binary_search(target, arr)
                    print(f"Search of {target} in {arr} => Index: {result}")
            else:
                arr = list(map(int, input("Enter sorted array: ").split()))
                print(arr)
                target = int(input("Enter target value: "))
                result = binary_search(target, arr)
                print(f"Search of {target} in {arr} => Index: {result}")
        
        elif choice == "2":  # BFS
            city_map = Graph()
    
            if mode != "y":
                edges = []
                number_of_edge = int(input("Enter the number of connexion of your city map:"))
                print('your edge connexion should look like this A B. It means that edge 1 connect node A and B')
                for i in range(0, number_of_edge):
                    edge = tuple(map(str, input(f"Nodes connected by edge {i}: ").split()))
                    edges.append(edge)
                    print(edges)
                for edge in edges:
                    city_map.add_edge(*edge)
                city_map.display()
                
                test = input('Do you want to test bfs (Y/N)').strip().lower()
                if test == 'y':
                    start = input("add a start node of you graph: ")
                    print(f"\nBFS From {start}:", bfs(city_map.graph, start))
                    print(f"DFS (recursif) from {start}:", dfs_recursive(city_map.graph, start))
                    print(f"DFS (iterative) from {start}:", dfs_iterative(city_map.graph, start))
                is_shortest = input('Do you want to see the short path between two path? (Y/N): ').strip().lower()
                if is_shortest == 'y':
                    nodes = list(input("provide the two node (example A B): ").split())
                    node1, node2 = nodes[0], nodes[1]
                    print(f"\nThe shortest path between {node1} and {node2}:", shortest_path_bfs(city_map.graph, node1, node2))
            else:
                edges = [
                    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), 
                    ("D", "F"), ("E", "F"), ("E", "G"), ("F", "G")
                ]

                for edge in edges:
                    city_map.add_edge(*edge)

                # Diplay graoh
                print("Graph that reprsent the city:")
                print(f"A=Mimbomane, B=Terminus, C=Post, D=Mobile Essos, E=Camer F=Omnisport, G=Titi garage")
                city_map.display()

                # Test BFS et DFS
                print("\nBFS From A:", bfs(city_map.graph, "A"))
                print("DFS (recursif) from A:", dfs_recursive(city_map.graph, "A"))
                print("DFS (iterative) from A:", dfs_iterative(city_map.graph, "A"))

                # check connectivity  and search of the shorted path
                print("\nThe shortest path between A et G:", shortest_path_bfs(city_map.graph, "A", "G"))
                print("The shortest path between B et E:", shortest_path_bfs(city_map.graph, "B", "E"))
                print("The shortest path between D et G:", shortest_path_bfs(city_map.graph, "D", "G"))
                print("The shortest path between A et X:", shortest_path_bfs(city_map.graph, "A", "X"))  # Test with node does not exist
        
        elif choice == "3":  # Knapsack
            if mode == "y":
                # list of object as form (value, wight)
                items = [(60, 10), (100, 20), (120, 30)]
                # maximale capacity of knapsack
                max_weight = 50
                max_value, selected_items = knapsack(items, max_weight)
                print(f"maximum possible value : {max_value}")
                print(f"Object selected : {selected_items}")
            else:
                n = int(input("enter the number of object: "))
                items = []
                for i in range(0, n):
                    obj = tuple(map(int, input(f"(value, weight) of object {i}: ").split()))
                    items.append(obj)
                    print(items)
                max_weight = int(input("Enter max weight of Knapsack: "))
                max_value, selected_items = knapsack(items, max_weight)
                print(f"maximum possible value : {max_value}")
                print(f"Object selected : {selected_items}")
        
        elif choice == "4":  # Merge Intervals
            if mode == "y":
                intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
                merged_intervals = merge_intervals(intervals)

                print(f"Merged intervals : {merged_intervals}")
                # Case where intervalle are not overlap
                merged_intervals = merge_intervals([(1, 2), (3, 4), (5, 6)])
                print(f"Merged intervals : {merged_intervals}")  

                # Case where we have overlapping
                merged_intervals = merge_intervals([(1, 5), (2, 6), (3, 7)])
                print(f"Merged intervals : {merged_intervals}")  

                # Case with one interval
                merged_intervals = merge_intervals([(5, 10)])
                print(f"Merged intervals : {merged_intervals}")  
            else:
                intervals = [tuple(map(int, input("Enter interval (start end): ").split())) for _ in range(int(input("Enter number of intervals: ")))]
                print("Merged intervals:", merge_intervals(intervals))
        
        elif choice == "5":  # Maximum Subarray Sum
            if mode == "y":
                # case 0
                arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                max_sum, subarray = max_subarray_sum(arr)
                print(f"case 1:\n max sum: {max_sum}, Corresponding subarray : {subarray}")

                # case 2
                max_sum, subarray = max_subarray_sum([1, 2, 3, 4, 5])
                print(f"case 2: \n max sum: {max_sum}, Corresponding subarray : {subarray}")   

                # case 3
                max_sum, subarray = max_subarray_sum([-1, -2, -3, -4])
                print(f"case 3: \n max sum: {max_sum}, Corresponding subarray : {subarray}")  

                # case 3:
                max_sum, subarray = max_subarray_sum([5, -1, -2, 10, -3, 2])

                print(f"case 4: \n max sum: {max_sum}, Corresponding subarray : {subarray}")  
            else:
                arr = list(map(int, input("Enter array: ").split()))
                max_sum, subarray = max_subarray_sum(arr)
                print(f"\n max sum: {max_sum}, Corresponding subarray : {subarray}")  


if __name__ == "__main__":
    main()
    