#include <cmath>
#include <iostream>
#include <chrono>
#include <fstream>

int main()
{
    int L1_cache_size = 32 * 1024 / (3 * sizeof(double));       // in double
    int L2_cache_size = 256 * 1024 / (3 * sizeof(double));  // in double
    int L3_cache_size = 12 * 1024 * 1024 / (3 * sizeof(double)); // in double

    std::ofstream csv_file("time_consumed2.csv");
    csv_file << "Array Size used (KBytes),time in ns\n";

    std::cout << "L1 cache size: " << L1_cache_size << " doubles" << std::endl;
    std::cout << "L2 cache size: " << L2_cache_size << " doubles" << std::endl;
    std::cout << "L3 cache size: " << L3_cache_size << " doubles" << std::endl;

    size_t array_sizes[21] = {0};

    for (int i = 0; i < 21; i++)
    {
        array_sizes[i] = (1024 * (pow(2, i))) / (3 * 8) + 1;
        std::cout << "Array size: " << array_sizes[i] << " doubles" << std::endl;
    }
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;

    for (int i = 0; i < 21; i++)
    {

        double *array_A = new double[array_sizes[i]];
        double *array_B = new double[array_sizes[i]];
        double *array_C = new double[array_sizes[i]];

        for (int i = 0; i < array_sizes[i]; ++i)
        {
            array_A[i] = static_cast<double>(std::rand()) / RAND_MAX;
            array_B[i] = static_cast<double>(std::rand()) / RAND_MAX;
            array_C[i] = 0.0;
        }

        auto start_time = std::chrono::high_resolution_clock::now();

        for (int l = 0; l < 20 * array_sizes[20] / array_sizes[i]; l++)
        {
            for (int l_i = 0; l_i < array_sizes[i]; l_i++)
            {
                array_C[l_i] = array_A[l_i] * 2.0;
            }
            
            for (int l_i = 0; l_i < array_sizes[i]; l_i++)
            {
                array_B[l_i] = array_A[l_i] * 2.0;
            }
        }

        auto end_time = std::chrono::high_resolution_clock::now();

        std::chrono::duration<double, std::nano> duration = end_time - start_time;

        std::cout << "duration: " << duration.count() << " ns" << std::endl;

        double time_per_element = duration.count() / (20 * array_sizes[20] / array_sizes[i] * array_sizes[i] * 3);

        csv_file << pow(2, i) << "," << time_per_element << "\n";

        delete[] array_A;
        delete[] array_B;
        delete[] array_C;
    }
    csv_file.close();
    std::cout << "finished" << std::endl;
    return 0;
}