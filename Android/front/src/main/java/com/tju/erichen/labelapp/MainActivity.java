package com.tju.erichen.labelapp;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;

import com.zhy.http.okhttp.OkHttpUtils;
import com.zhy.http.okhttp.callback.BitmapCallback;
import com.zhy.http.okhttp.callback.StringCallback;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

import okhttp3.Call;




public class MainActivity extends AppCompatActivity {

    private ImageView image;
    Button button1;
    Button button2;
    Button button3;
    Button button_last;
    Button button_next;
    TextView textView1;
    TextView textView2;
    TextView textView3;
    Spinner spinner1_1;
    Spinner spinner1_2;
    Spinner spinner2_1;
    Spinner spinner2_2;
    Spinner spinner3_1;
    Spinner spinner3_2;
    int index;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        index = 0;
        image = (ImageView) findViewById(R.id.imageView);
        OkHttpUtils.get().url("http://192.168.1.148:5000/image"+index+"").build().execute(new BitmapCallback() {

            @Override
            public void onResponse(Bitmap bitmap, int i) {
                try {
                    image.setImageBitmap(bitmap);
                } catch (Exception e) {
                }
            }

            @Override
            public void onError(Call arg0, Exception arg1, int arg2) {
                // TODO Auto-generated method stub

            }
        });


        textView1 = (TextView)findViewById(R.id.editText1);
        textView2 = (TextView)findViewById(R.id.editText2);
        textView3 = (TextView)findViewById(R.id.editText3);
        OkHttpUtils.get().url("http://192.168.1.148:5000/text"+index+"").build().execute(new StringCallback() {
            @Override
            public void onError(Call call, Exception e, int id) {

            }

            @Override
            public void onResponse(String response, int id) {
                String[] r = response.split("@");
                textView3.setText(r[2]);
                textView1.setText(r[0]);
                textView2.setText(r[1]);
            }
        });

        spinner1_1 = (Spinner)findViewById(R.id.spinner1_1);
        spinner1_2 = (Spinner)findViewById(R.id.spinner1_2);
        spinner2_1 = (Spinner)findViewById(R.id.spinner2_1);
        spinner2_2 = (Spinner)findViewById(R.id.spinner2_2);
        spinner3_1 = (Spinner)findViewById(R.id.spinner3_1);
        spinner3_2 = (Spinner)findViewById(R.id.spinner3_2);

        button1 = (Button)findViewById(R.id.button1);
        button2 = (Button)findViewById(R.id.button2);
        button3 = (Button)findViewById(R.id.button3);
        button_last = (Button)findViewById(R.id.lastbutton);
        button_next = (Button)findViewById(R.id.nextbutton);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String t1 = (String)spinner1_1.getSelectedItem();
                String t2 = (String)spinner1_2.getSelectedItem();
                textView1.setText("a " + t2 + " bridge is on a " + t1 + " river");

            }
        });
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String t1 = (String)spinner2_1.getSelectedItem();
                String t2 = (String)spinner2_2.getSelectedItem();
                textView2.setText("the " + t1 + " part of the bridge " + t2);
            }
        });
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String t1 = (String)spinner3_1.getSelectedItem();
                String t2 = (String)spinner3_2.getSelectedItem();
                textView3.setText(t2 + " on the " + t1 + " part of the bridge");
            }
        });

        button_last.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url = "http://192.168.1.148:5000/text"+index+"";
                OkHttpUtils.get().url(url).build().execute(new StringCallback() {
                    @Override
                    public void onError(Call call, Exception e, int id) {

                    }

                    @Override
                    public void onResponse(String response, int id) {
                        String[] r = response.split("@");
                        textView3.setText(r[2]);
                        textView1.setText(r[0]);
                        textView2.setText(r[1]);
                    }
                });
                OkHttpUtils.get().url("http://192.168.1.148:5000/image"+index+"").build().execute(new BitmapCallback() {

                    @Override
                    public void onResponse(Bitmap bitmap, int i) {
                        try {
                            image.setImageBitmap(bitmap);
                        } catch (Exception e) {
                        }
                    }

                    @Override
                    public void onError(Call arg0, Exception arg1, int arg2) {
                        // TODO Auto-generated method stub

                    }
                });
                index = index - 1;
                if(index < 0){
                    index = 0;
                }
            }
        });

        button_next.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                OkHttpUtils.get().url("http://192.168.1.148:5000/text"+index+"").build().execute(new StringCallback() {
                    @Override
                    public void onError(Call call, Exception e, int id) {

                    }

                    @Override
                    public void onResponse(String response, int id) {
                        String[] r = response.split("@");
                        textView3.setText(r[2]);
                        textView1.setText(r[0]);
                        textView2.setText(r[1]);
                    }
                });
                OkHttpUtils.get().url("http://192.168.1.148:5000/image"+index+"").build().execute(new BitmapCallback() {

                    @Override
                    public void onResponse(Bitmap bitmap, int i) {
                        try {
                            image.setImageBitmap(bitmap);
                        } catch (Exception e) {
                        }
                    }

                    @Override
                    public void onError(Call arg0, Exception arg1, int arg2) {
                        // TODO Auto-generated method stub

                    }
                });
                index = index + 1;
                if(index == 1000){
                    index = 999;
                }
            }
        });


    }

}
