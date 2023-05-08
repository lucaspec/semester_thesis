package com.example.yolo_app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import org.pytorch.LiteModuleLoader;
import org.pytorch.Module;
import org.pytorch.Tensor;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Random;


public class MainActivity extends AppCompatActivity {

    // Elements in the view
    Button btnGenerate;
    ImageView ivImage;
    TextView tvWaiting;

    // Tag used for logging
    private static final String TAG = "MainActivity";

    // PyTorch model
    Module module;

    // Size of the input tensor
    int inSize = 512;

    // Width and height of the output image
    int width = 256;
    int height = 256;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Get the elements in the activity
        btnGenerate = findViewById(R.id.btnGenerate);
        ivImage = findViewById(R.id.ivImage);
        tvWaiting = findViewById(R.id.tvWaiting);

        // Load in the model
        try {
            module = LiteModuleLoader.load(assetFilePath("yolov7-tiny.torchscript.ptl"));
        } catch (IOException e) {
            Log.e(TAG, "Unable to load model", e);
        }
    }

    // Given the name of the pytorch model, get the path for that model
    public String assetFilePath(String assetName) throws IOException {
        File file = new File(this.getFilesDir(), assetName);
        if (file.exists() && file.length() > 0) {
            return file.getAbsolutePath();
        }

        try (InputStream is = this.getAssets().open(assetName)) {
            try (OutputStream os = new FileOutputStream(file)) {
                byte[] buffer = new byte[4 * 1024];
                int read;
                while ((read = is.read(buffer)) != -1) {
                    os.write(buffer, 0, read);
                }
                os.flush();
            }
            return file.getAbsolutePath();
        }
    }




}