# Copy over your a1_partc.py file here

class Stack:
    # Constructor of the list, default the capacity to 10
    def __init__(self, cap=10):
        self._capacity = cap
        # Initial the stack to None
        self.stack = [None] * self._capacity
        self.size = 0

    def capacity(self):
        return self._capacity

    def push(self, data):
        # Check if stack is full
        if self.size == self._capacity:
            # Double the capacity
            new_list_capacity = self._capacity * 2
            new_list = [None] * new_list_capacity

            # Copy the elements to the new list
            for i in range(self._capacity):
                new_list[i] = self.stack[i]
            # Replace the current stack by new list
            self.stack = new_list
            self._capacity = new_list_capacity

        # Add the new element to the stack
        self.stack[self.size] = data
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        self.size -= 1
        # Hold the data to be deleted for return
        data = self.stack[self.size]
        self.stack[self.size] = None
        return data

    def get_top(self):
        return self.stack[self.size - 1] if self.size > 0 else None

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class Queue:
    # Constructor of the queue, default the capacity to 10
    def __init__(self, cap=10):
        self._capacity = cap
        # Initial the queue to safe status
        self.queue = [None] * self._capacity
        self.size = 0

    def capacity(self):
        return self._capacity

    def enqueue(self, data):
        if self.size == self._capacity:
            # If the Queue is full, double the size
            new_capacity = self._capacity * 2
            new_queue = [None] * new_capacity

            # Copy elements to the new queue
            for i in range(self.size):
                new_queue[i] = self.queue[i]
            # Replace the current queue by new queue
            self.queue = new_queue
            self._capacity = new_capacity

        self.queue[self.size] = data
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        # Hold the data to be deleted for return
        data = self.queue[0]
        # Copy whole queue from index 1 and the rest of the queue
        for i in range(1, self.size):
            self.queue[i - 1] = self.queue[i]
        # Resize the queue
        self.size -= 1
        self.queue[self.size] = None
        return data
    
    # Getter of the front
    def get_front(self):
        if self.size == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return self.size == 0

    # Getter of the current queue size
    def __len__(self):
        return self.size


class Deque:
    # Constructor of deque, default capacity is 10
    def __init__(self, cap=10):
        self._capacity = cap
        self.front_index = 0
        self.size = 0
        self.deque = [None] * self._capacity

    def capacity(self):
        return self._capacity

    def push_front(self, data):
        # Double the size of deque when it is full
        if self.size == self._capacity:
            # Helper function
            self.resize(self._capacity * 2)
        # Update the front_index, as push front so the index -1 to
        # indicate the shift of new front_index
        self.front_index = (self.front_index - 1) % len(self.deque)
        # push the data to the front
        self.deque[self.front_index] = data
        self.size += 1

    def push_back(self, data):
        # Double the size of deque when it is full
        if self.size == self._capacity:
            self.resize(self._capacity * 2)
        # Update the back_index
        back_index = (self.front_index + self.size) % self._capacity
        # push the data to the back
        self.deque[back_index] = data
        self.size += 1
        return True 

    def pop_front(self):
        if self.size == 0:
            raise IndexError('pop_front() used on empty deque')
        # Hold the data to be deleted for return
        data = self.deque[self.front_index]
        # Delete the value in deque
        self.deque[self.front_index] = None
        # Revised the front index
        self.front_index = (self.front_index + 1) % self._capacity
        self.size -= 1
        return data

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        # Calculate the last index of data, % len(self.deque) to ensure wrapping
        # the case of circular behavior
        back_index = (self.front_index + self.size - 1) % len(self.deque)
        # Hold the data to be deleted for return
        data = self.deque[back_index]
        # Manually pop the target data
        self.deque[back_index] = None
        # resize the deque
        self.size -= 1
        return data

    def get_front(self):
      if self.size == 0:
          return None
      return self.deque[self.front_index]

    def get_back(self):
      if self.size == 0:
          return None  # or raise an exception if you prefer
      back_index = (self.front_index + self.size - 1) % self._capacity
      return self.deque[back_index]

    def is_empty(self):
      return self.size == 0

    def __len__(self):
      return self.size

    def __getitem__(self, k):
        if k < 0 or k >= self.size:
            raise IndexError('Index out of range')
        return self.deque[(self.front_index + k) % self._capacity]
        
    # Helper function
    def resize(self, newCap):
      # Temp hold the current deque
      temp_deque = self.deque
      # Resize and initialize the current deque
      self.deque = [None] * newCap
      # Migrate the data from old deque to new size deque
      for i in range(self.size):
          self.deque[i] = temp_deque[(self.front_index + i) % len(temp_deque)]
      # Update new front index and new capacity according to new size
      self.front_index = 0
      self._capacity = newCap
