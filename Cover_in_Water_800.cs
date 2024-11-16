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
                // string[] n_x = first.Split(' ');
                int n = Convert.ToInt32(first);
                // int x = Convert.ToInt32(n_x[1]);

                // int[] arr = new int[n];
                string second = Console.ReadLine();

                int res=0;
                for(int i=0;i<n;i++){
                    if(second[i]=='.'){
                        int cnt = 0;
                        while(i<n && second[i]=='.'){
                            cnt++;
                            i++;
                        }
                        if(cnt>2){
                            res = 2;
                            break;
                        }else {
                            res += cnt;
                        }
                    }
                }

                Console.WriteLine(res);

                t--;
            }
        }
    }
}
