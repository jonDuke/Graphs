import random
from collections import deque

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        
        # Generate all possible friendships combinations
        # Avoid duplicates by ensuring 1st < 2nd
        possible = []
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible.append((user_id, friend_id))

        # Shuffle friendships
        random.shuffle(possible)

        # Create N friendships, where N = num_users * avg_friendships / 2
        for i in range(num_users * avg_friendships // 2):
            self.add_friendship(*possible[i])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        # Perform breadth first search and save shortest path to each node
        # Start a queue with the initial user_id        
        visited = {user_id : [user_id]}
        q = deque()
        q.append(user_id)

        while len(q) > 0:  # while the queue is not empty
            current = q.popleft()
            for friend in self.friendships[current]: # check each friend
                # if we haven't already found a path to this friend...
                if friend not in visited:
                    # the shortest path is the path to current + friend
                    visited[friend] = visited[current].copy()
                    visited[friend].append(friend)
                    
                    q.append(friend)  # add this friend to the queue

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print("Friendships:")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("Connections to id 1:")
    print(connections)
