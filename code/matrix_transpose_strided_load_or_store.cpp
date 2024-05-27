#include <iostream>
#include <chrono>
#include <fstream>

int main()
{

    /*
     elemente die man benötigt um L1 cache auszureizen:
     32KB *1024 / 8 = 4096 double elemente
     4096/2 = 2048 elemente jeweils für A und B
        2048^(1/2) = 45.25 -> 45x45 matrix

    elemente die man benötigt um L2 cache auszureizen:
     256KB * 1024 / 8 = 32768 double elemente
     32768/2 = 16384 elemente jeweils für A und B
        16384^(1/2) = 128 -> 128x128 matrix
    
    elemente die man benötigt um L3 cache auszureizen:
     12MB * 1024*1024 / 8 = 1572864 double elemente
        1572864/2 = 786432 elemente jeweils für A und B
        786432^(1/2)  -> 886x886 matrix


    */
    size_t dimension_sizes[30] = {10, 20, 30, 40, 60, 70, 100, 120, 130,
                                  150, 180, 200, 220, 250, 280, 300, 400, 500, 750, 850, 900, 1000, 1300, 1500, 1900, 2300, 2700, 2800, 2900, 3000};

    const size_t sizes = sizeof(dimension_sizes) / sizeof(dimension_sizes[0]);

    std::ofstream csv_file("memory_bandwidth__transpose_strided_store.csv");
    csv_file << "Array Size ,Bandwidth (GB/s)\n";

    for (size_t size_idx = 0; size_idx < sizes; ++size_idx)
    {
        const size_t array_size = dimension_sizes[size_idx];

        double *array_A = new double[array_size * array_size];
        double *array_B = new double[array_size * array_size];

        for (size_t l_y = 0; l_y < array_size; ++l_y)
        {
            for (size_t l_x = 0; l_x < array_size; ++l_x)
            {
                array_A[l_y * array_size + l_x] = static_cast<double>(std::rand()) / RAND_MAX;
            }
        }

        auto start_time = std::chrono::high_resolution_clock::now();
        for (size_t iteration = 0; iteration < 10000 * (dimension_sizes[29] / array_size); ++iteration)
        {
            for (size_t l_y = 0; l_y < array_size; ++l_y)
            {
                for (size_t l_x = 0; l_x < array_size; ++l_x)
                {
                    array_B[l_x*array_size+l_y] = array_A[array_size* l_y+ l_x];
                }
            }
        }
        auto end_time = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> duration = end_time - start_time;

        double data_access_speed = 10000 * (dimension_sizes[29] / array_size) * 2.0 * array_size * array_size * sizeof(double) / (duration.count() / 1000) / (1024 * 1024 * 1024);
        csv_file << array_size<<","<<data_access_speed <<std::endl;
        delete[] array_A;
        delete[] array_B;
    }
    csv_file.close();
    std::cout << "finished." << std::endl;
    return 0;
}
