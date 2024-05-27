#include <iostream>
#include <chrono>
#include <cstdlib>
#include <fstream>
int main()
{
  double l_scalar = 2.0;
  size_t l_array_sizes[] = {
      32, 48, 64, 96, 128, 192, 256, 384, 512, 768,
      1024, 1536, 2048, 3072, 4096, 6144, 8192, 12288,
      16384, 24576, 32768, 49152, 65536, 98304, 131072,
      196608, 262144, 393216, 524288, 786432, 1048576,
      1572864, 2097152,2597152,3097152};

  int l_array_sizes_count = sizeof(l_array_sizes) / sizeof(l_array_sizes[0]);

  std::ofstream csv_file("memory_bandwidth.csv");
  csv_file << "Array Size (bytes), Bandwidth (GB/s)\n";

  for (int i = 0; i < l_array_sizes_count; i++)
  {

    double *l_A = new double[l_array_sizes[i]];
    double *l_B = new double[l_array_sizes[i]];
    double *l_C = new double[l_array_sizes[i]];

    for (int j = 0; j < l_array_sizes[i]; ++j)
    {
      l_A[j] = static_cast<double>(std::rand()) / RAND_MAX;
      l_B[j] = static_cast<double>(std::rand()) / RAND_MAX;
      l_C[j] = 0.0;
    }

    auto l_start_time = std::chrono::high_resolution_clock::now();
    for (int k = 0; k < 10000 *(l_array_sizes[32]/l_array_sizes[i]); ++k)
    {
      for (int l = 0; l < l_array_sizes[i]; ++l)
      {
        l_C[l] = l_A[l] + l_scalar * l_B[l];
      }
    }

    auto l_end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::micro> l_duration = l_end_time - l_start_time;

    double l_data_access_speed = 10000 * ((l_array_sizes[32]/l_array_sizes[i]) * 3.0 * l_array_sizes[i] * sizeof(double) / (l_duration.count() / 1e6) / (1024 * 1024 * 1024));
    csv_file << l_array_sizes[i] * 3 << " , " << l_data_access_speed << std::endl;

    delete[] l_A;
    delete[] l_B;
    delete[] l_C;
  }
  csv_file.close();
  return 0;
}
// (l_array_sizes[32]/l_array_sizes[i]) is the number of iterations in the loop
// 3.0 is the number of arrays accessed in the loop
// l_array_sizes[i] is the size of each array in bytes
// sizeof(double) is the size of each element in bytes (8 bytes)
// l_duration.count() is the time taken in seconds
// 1e6 is the conversion factor from microseconds to seconds
// (1024 * 1024 * 1024) is the conversion factor from bytes to GB