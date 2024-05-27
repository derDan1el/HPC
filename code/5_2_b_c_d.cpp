#include <iostream>
#include <algorithm>
#include <random>
#include <chrono>
#include <fstream>
#include <string>

void gemm_row(double *X, double *Y, double *Z, int n)
{
    for (std::size_t l_m = 0; l_m < n; l_m++)
    {
        for (std::size_t l_k = 0; l_k < n; l_k++)
        {
            for (std::size_t l_n = 0; l_n < n; l_n++)
            {
                Z[l_m * n + l_n] += X[l_m * n + l_k] * Y[l_k * n + l_n];
            }
        }
    }
}

void gemm_column(double *X,
                 double *Y,
                 double *Z,
                 int n)
{

    for (std::size_t l_n = 0; l_n < n; l_n++)
    {
        for (std::size_t l_k = 0; l_k < n; l_k++)
        {
            for (std::size_t l_m = 0; l_m < n; l_m++)
            {
                Z[l_m * n + l_n] += X[l_m * n + l_k] * Y[l_k * n + l_n];
            }
        }
    }
}

void gemm_blocked(double *X,
                  double *Y,
                  double *Z,
                  int n,
                  int blockSize)
{
    std::size_t nBlocks = n / blockSize;
    for (std::size_t l_bm = 0; l_bm < nBlocks; l_bm++)
    {
        for (std::size_t l_bn = 0; l_bn < nBlocks; l_bn++)
        {
            for (std::size_t l_bk = 0; l_bk < nBlocks; l_bk++)
            {
                for (std::size_t l_m = l_bm * blockSize; l_m < (l_bm + 1) * blockSize; l_m++)
                {
                    for (std::size_t l_k = l_bk * blockSize; l_k < (l_bk + 1) * blockSize; l_k++)
                    {
                        for (std::size_t l_n = l_bn * blockSize; l_n < (l_bn + 1) * blockSize; l_n++)
                        {
                            Z[l_m * n + l_n] += X[l_m * n + l_k] * Y[l_k * n + l_n];
                        }
                    }
                }
            }
        }
    }
}

int check_arguments(int argc, char **argv, std::string &mode)
{
    if (argc != 2)
    {
        std::cerr << "Usage: " << argv[0] << " <mode>" << std::endl;
        return 1;
    }
    if (std::string(argv[1]) == "row")
    {
        std::cout << "use Row-Major MMM" << std::endl;
        mode = "row";
    }
    else if (std::string(argv[1]) == "col")
    {
        std::cout << "use Column-Major MMM" << std::endl;
        mode = "col";
    }
    else if (std::string(argv[1]) == "block")
    {
        std::cout << "use Blocked MMM" << std::endl;
        mode = "block";
    }
    else
    {
        std::cerr << "you can only choose between 'row' , 'col' , 'block' " << std::endl;
        return 1;
    }
    return 0;
}
int main(int argc, char **argv)
{

    // es wird überprüft ob die Argumente korrekt sind und mode gesetzt
    std::string mode = "";
    if (check_arguments(argc, argv, mode))
    {
        return 1;
    }

    // CSV-Datei erstellen
    std::string filename = "5_2_" + mode + ".csv";
    std::ofstream file(filename);
    file << "n,time" << std::endl;

    // Zufallsgenerator schaffen
    std::mt19937 random(std::random_device{}());
    std::uniform_real_distribution<double> dist(0.0, 1.0);

    // Größen der Matrizen
    int sizes[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1536, 2048, 2560, 3072, 3584, 4096};

    for (int n : sizes)
    {
        std::cout << "zurzeit wird folgendes n abgearbeitet n = " << n << std::endl;
        // Anzahl der Wiederholungen abhängig von der Größe der Matrix festlegen
        // damit man nicht bei großen n zu lange rechnet
        int reps = std::max(100000 / (n * 50), 1);
        double time = 0;

        // speicher allozieren
        double *X = new double[n * n];
        double *Y = new double[n * n];
        double *Z = new double[n * n];

        for (int i = 0; i < reps; i++)
        {
            // Zeitmessung
            for (int i = 0; i < n * n; i++)
            {
                X[i] = dist(random);
                Y[i] = dist(random);
                Z[i] = 0;
            }
            auto start = std::chrono::high_resolution_clock::now();
            if (mode == "row")
            {
                gemm_row(X, Y, Z, n);
            }
            else if (mode == "col")
            {
                gemm_column(X, Y, Z, n);
            }
            else if (mode == "block")
            {
                // wenn n >= 512 dann blockSize = 512 sonst kein blocking
                gemm_blocked(X, Y, Z, n, n >= 256 ? 256 : n);
            }
            auto end = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> diff = end - start;
            time += diff.count();
        }
        // durchschnittswert der Zeit ermitteln
        time /= reps;

        // Zeit in CSV-Datei schreiben
        file << n << "," << time << std::endl;

        delete[] X;
        delete[] Y;
        delete[] Z;
    }
    file.close();
    return 0;
}