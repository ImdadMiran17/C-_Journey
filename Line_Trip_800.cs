using System;
using System.Security.Cryptography.X509Certificates;

namespace NewJourney
{
    class Program
    {
        static void Main(string[] args)
        {
            int t = Convert.ToInt32(Console.ReadLine());
            while(t>0){
                string first = Console.ReadLine();
                string[] n_x = first.Split(' ');
                int n = Convert.ToInt32(n_x[0]);
                int x = Convert.ToInt32(n_x[1]);

                int[] arr = new int[n];
                string[] second = Console.ReadLine().Split(' ');

                int ans=0, prev=0;
                for(int i = 0; i<n; i++){
                    arr[i] = Int32.Parse(second[i]);
                    ans = Math.Max(ans, arr[i] - prev);
                    prev = arr[i];
                }

                ans = Math.Max(ans, 2*(x - prev));
                Console.WriteLine(ans);
                t--;
            }
        }
    }
}
