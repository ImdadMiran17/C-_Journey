using System;

namespace NewJourney
{
    class Program
    {
        static bool IsSorted(int[] arr){
            for(int i=1;i<arr.Length;i++){
                if(arr[i-1] > arr[i])
                    return false;
            }
            return true;
        }
        static void Main(string[] args)
        {
            int t = Convert.ToInt32(Console.ReadLine());
            while(t>0){
                string first = Console.ReadLine();
                string[] n_k = first.Split(' ');
                int n = Convert.ToInt32(n_k[0]);
                int k = Convert.ToInt32(n_k[1]);

                int[] arr = new int[n];
                string[] second = Console.ReadLine().Split(' ');
                for(int i = 0; i<n; i++){
                    arr[i] = Int32.Parse(second[i]);
                }

                bool con = IsSorted(arr);

                if(n == 1){
                    Console.WriteLine("YES");
                }
                else if(con==false && k==1){
                    Console.WriteLine("NO");
                }
                else{
                    Console.WriteLine("YES");
                }

                t--;
            }
        }
    }
}
