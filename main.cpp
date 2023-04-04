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
    

    cout<<endl<<"1. encryption\n2. decryption\n3. setup files\n4. exit\n"<<endl;
    cin>>wyb;

    switch (wyb)
    {
        case '1':
        {
            string key, file, output,mode;
            mode = "encrypt";
            cout<<endl<<"encryption key: "; cin>>key;
            cout<<endl<<"File Location: "; cin>>file;
            cout<<endl<<"Output File Location and name: "; cin>>output;
            cout<<endl<<"Work in progress..."<<endl;


            crypto(mode,key,file,output);

            break;
        }
        case '2':
        {
            string key, file, output,mode;
            mode = "decrypt";
            cout<<endl<<"decryption key: "; cin>>key;
            cout<<endl<<"File Location: "; cin>>file;
            cout<<endl<<"Output File Location and name: "; cin>>output;
            cout<<endl<<"Work in progress..."<<endl;

            

            crypto(mode,key,file,output);

            break;
        }
        case '3':
        {
            string cmd = "pip install -r py_lib/requirements.txt";
            system(cmd.c_str());
            cout<<endl<<"succes! "<<endl;
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

    cout<<endl<<"executed! "<<endl;
    getchar(); getchar();
    


}