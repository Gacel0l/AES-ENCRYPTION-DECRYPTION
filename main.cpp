#include <iostream>
#include <string>

using namespace std;

char wyb;


string crypto(string mode, string key, string file, string output)
{
  
    if(mode == "encrypt")
    {
        string cmd = "python py_lib/crypto.py encrypt -k \"" +key+"\" -f \"" +file+"\" -o \"" +output + "\"";
        system(cmd.c_str());
    }
    else
    {
        string cmd = "python py_lib/crypto.py decrypt -k \"" +key+"\" -f \"" +file+"\" -o \"" +output + "\"";
        system(cmd.c_str());
    }


    return "0";
}

int main()
{
    

    cout<<endl<<"1. szyfrowanie 2. odszyfrowywanie 3. zainstaluj 4. wyjscie"<<endl;
    cin>>wyb;

    switch (wyb)
    {
        case '1':
        {
            string key, file, output,mode;
            mode = "encrypt";
            cout<<endl<<"podaj klucz: "; cin>>key;
            cout<<endl<<"podaj plik: "; cin>>file;
            cout<<endl<<"podaj plik wyjsciowy: "; cin>>output;
            cout<<endl<<"Praca w toku..."<<endl;


            crypto(mode,key,file,output);

            break;
        }
        case '2':
        {
            string key, file, output,mode;
            mode = "decrypt";
            cout<<endl<<"podaj klucz: "; cin>>key;
            cout<<endl<<"podaj plik: "; cin>>file;
            cout<<endl<<"podaj plik wyjsciowy: "; cin>>output;
            cout<<endl<<"Praca w toku..."<<endl;

            

            crypto(mode,key,file,output);

            break;
        }
        case '3':
        {
            string cmd = "pip install -r py_lib/requirements.txt";
            system(cmd.c_str());
            cout<<endl<<"zainstalowano! "<<endl;
            break;
        }
        case '4':
        {
            cout<<endl<<"BYE!"<<endl;
            return 0;
            break;
        }









        default:
        {
            main();
        }
        break;


        main();

    }

    cout<<endl<<"wykonano! "<<endl;
    getchar(); getchar();
    


}