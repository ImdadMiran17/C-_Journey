// using System;
// using System.Security.Cryptography.X509Certificates;

namespace NewJourney
{
    class Program
    {
        static void Main(string[] args)
        {
            int t = Convert.ToInt32(Console.ReadLine());
            while(t>0){
                string first = Console.ReadLine();
                // string[] n_x = first.Split(' ');
                int n = Convert.ToInt32(first);
                // int x = Convert.ToInt32(n_x[1]);

                // int[] arr = new int[n];
                // string second = Console.ReadLine();

                if(n%3==0){
                    Console.WriteLine("Second");
                }else{
                    Console.WriteLine("First");
                }

                t--;
            }
        }
    }
}
