#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char wyb;


string crypto(string mode, string key, string file, string output)
{
  
    if(mode == "encrypt")
    {
        string cmd = "python py_lib/crypto.py encrypt -k \"" +key+"\" -f \"" +file+"\" -o \"" +output + "\"";
        system(cmd.c_str());
    }
    else if (mode == "decrypt")
    {
        string cmd = "python py_lib/crypto.py decrypt -k \"" +key+"\" -f \"" +file+"\" -o \"" +output + "\"";
        system(cmd.c_str());
    }
    else if (mode == "d_encrypt")
    {
        string cmd = "python py_lib/crypto.py encrypt -k \"" +key+"\" -d \"" +file+"\"";
        system(cmd.c_str());
    }
    else if (mode == "d_decrypt")
    {
        string cmd = "python py_lib/crypto.py decrypt -k \"" +key+"\" -d \"" +file+"\"";
        system(cmd.c_str());
    }


    return "0";
}


string PyS(string command, string data, string name)
{   


    if((command == "QR" || command == "1"))
    {
        string cmd = "python py_lib/qr.py -d \"" + data + "\" -n \"" + name + "\"";
        system(cmd.c_str());
    }
    else
    {
        return "1";
    }
    
    return "0";
}

string QR()
{
    string data, nazwa;
    cout<<endl<<"result file name: "<<endl;
    cin>>nazwa;
    cout<<"submit qr code data: "<<endl;
    cin>>data;


    PyS("QR", data, nazwa + ".png");
    return "0";
}


int main()
{
    
    cout<<endl<<"1. encryption\n2. decryption\n3. setup files\n4. pass-gen\n5. QR\n6. exit"<<endl;
    cin>>wyb;

    switch (wyb)
    {
        case '1':
        {       
            string odp;
            cout<<endl<<"1.encrypt file\n2.encrypt all files in directory"<<endl;
            cin>>odp;


            if(odp == "1")
            {
                 string key, file, output,mode;
                 mode = "encrypt";
                 cout<<endl<<"encryption key: "; cin>>key;
                 cout<<endl<<"File Location: "; cin>>file;
                 cout<<endl<<"Output File Location and name: "; cin>>output;
                 cout<<endl<<"Work in progress..."<<endl;
                 crypto(mode,key,file,output);
            }
            else if (odp == "2")
            {
                 string key, file, output,mode;
                 mode = "d_encrypt";
                 cout<<endl<<"encryption key: "; cin>>key;
                 cout<<endl<<"directory Location: "; cin>>file;
                 cout<<endl<<"Work in progress..."<<endl;
                 crypto(mode,key,file,output);
            }
            else
            {
                cout<<endl<<"WRONG ACTION! "<<endl;
            }
            

           


            

            break;
        }
        case '2':
        {
            string odp;
            cout<<endl<<"1.decrypt file\n2.decrypt all files in directory"<<endl;
            cin>>odp;

            if(odp == "1")
            {
                string key, file, output,mode;
                mode = "decrypt";
                cout<<endl<<"decryption key: "; cin>>key;
                cout<<endl<<"File Location: "; cin>>file;
                cout<<endl<<"Output File Location and name: "; cin>>output;
                cout<<endl<<"Work in progress..."<<endl;

            

                crypto(mode,key,file,output);

            }
            else if (odp == "2")
            {
                string key, file, output,mode;
                mode = "d_decrypt";
                cout<<endl<<"decryption key: "; cin>>key;
                cout<<endl<<"directory Location: "; cin>>file;
                cout<<endl<<"Work in progress..."<<endl;

            

                crypto(mode,key,file,output);
            }

           
            break;
        }
        case '3':
        {
            string cmd = "pip install -r py_lib/requirements.txt";
            system(cmd.c_str());
            cout<<endl<<"succes! "<<endl;
            break;
        }
        case '6':
        {
            cout<<endl<<"BYE!"<<endl;
            return 0;


            break;
        }
        case '4':
        {
            string password = "";
            double length = 32;
            cout<<endl<<"password length: ";
            cin>>length;
            string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;':\",./<>?";

            srand(time(0));

            for(int i = 0; i < length; i++)
            {
                int random_index = rand() % characters.length();
                password += characters[random_index];
            }

            cout<<endl<<password;
            ofstream save;
            save.open("pass.txt",ios_base::app);
            save<<password;
            save.close();
            cout<<endl<<endl<<"\n password saved in local directory [pass.txt]"<<endl;
            

            

            break;
        }
        case '5':
        {
            cout<<endl<<"you can enter your keys and passwords here to easily copy them on your phone"<<endl;
            QR();




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
    
    main();


}