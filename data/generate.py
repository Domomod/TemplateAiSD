#Remember to pip3 install numpy
import numpy as np

def generate_random_array(size):
    return np.random.randint(0, 10000, size, dtype=int)

def generate_increasing_array(size):
    return np.arange(size)

def generate_decreasing_array(size):
    return np.arange(size, 0, -1)

def generate_constant_array(size, value=42):
    return np.full(size, value)

def generate_a_shaped_array(size):
    half_size = size // 2
    increasing_part = np.arange(half_size)
    decreasing_part = np.arange(half_size, 0, -1)
    return np.concatenate((increasing_part, decreasing_part))

# Set the sizes for the arrays
sizes = [2**x for x in range(2, 20)]

for size in sizes:
    # Generate arrays
    random_array = generate_random_array(size)
    increasing_array = generate_increasing_array(size)
    decreasing_array = generate_decreasing_array(size)
    constant_array = generate_constant_array(size)
    a_shaped_array = generate_a_shaped_array(size)

    # Add instance size as the first number and save arrays to files
    np.savetxt(f'benchmark/random_array_{size:08d}.txt', np.insert(random_array, 0, size), fmt='%d')
    np.savetxt(f'benchmark/increasing_array_{size:08d}.txt', np.insert(increasing_array, 0, size), fmt='%d')
    np.savetxt(f'benchmark/decreasing_array_{size:08d}.txt', np.insert(decreasing_array, 0, size), fmt='%d')
    np.savetxt(f'benchmark/constant_array_{size:08d}.txt', np.insert(constant_array, 0, size), fmt='%d')
    np.savetxt(f'benchmark/a_shaped_array_{size:08d}.txt', np.insert(a_shaped_array, 0, size), fmt='%d')


print("Arrays have been generated and saved to files.")
