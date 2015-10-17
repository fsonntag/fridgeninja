package ninja.fridge.fridgeninja;

import android.app.Activity;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import org.altbeacon.beacon.Beacon;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;


/**
 * A simple {@link Fragment} subclass.
 * Use the {@link FridgeInterfaceFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class FridgeInterfaceFragment extends Fragment implements SensorEventListener, MatchedBeaconUpdateCallback {
    public void setCallback(FridgeCallback callback) {
        this.callback = callback;
    }

    @Override
    public void beaconsChanged(final Collection<BeaconBuffer.BeaconInfo> newBeacons) {
        mActivity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                View view = getView();
                if(view != null) {
                    adapter.clear();
                    adapter.addAll(newBeacons);
                    adapter.notifyDataSetChanged();
                }
            }
        });

    }
//    // TODO: Rename parameter arguments, choose names that match
//    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
//    private static final String ARG_PARAM1 = "param1";
//    private static final String ARG_PARAM2 = "param2";
//
//    // TODO: Rename and change types of parameters
//    private String mParam1;
//    private String mParam2;

    public interface FridgeCallback {
        public void opened();
        public void closed();
        public void startOpening();
        public void startClosing();
    }

    private MainActivity mActivity;
    private FridgeCallback callback;


    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @return A new instance of fragment FridgeInterfaceFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static FridgeInterfaceFragment newInstance() {
        FridgeInterfaceFragment fragment = new FridgeInterfaceFragment();
        Bundle args = new Bundle();
//        args.putString(ARG_PARAM1, param1);
//        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    public FridgeInterfaceFragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        if (getArguments() != null) {
//            mParam1 = getArguments().getString(ARG_PARAM1);
//            mParam2 = getArguments().getString(ARG_PARAM2);
//        }
    }

    ArrayAdapter<BeaconBuffer.BeaconInfo> adapter;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_fridge_interface, container, false);
        ((TextView)view.findViewById(android.R.id.empty)).setText("No beacons");
        adapter = new ArrayAdapter<BeaconBuffer.BeaconInfo>(mActivity, android.R.layout.simple_list_item_2,
                android.R.id.text1, new ArrayList<BeaconBuffer.BeaconInfo>()) {
            @Override
            public View getView(int position, View convertView, ViewGroup parent) {
                View view = super.getView(position, convertView, parent);
                TextView text1 = (TextView) view.findViewById(android.R.id.text1);
                TextView text2 = (TextView) view.findViewById(android.R.id.text2);

                BeaconBuffer.BeaconInfo info = getItem(position);

                text1.setText(info.beacon.getBluetoothAddress());
                text2.setText("Distance " + info.minDistance + "m");
                return view;
            }
        };
        ((ListView)view.findViewById(android.R.id.list)).setAdapter(adapter);
        return view;
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);

        try {
            mActivity = (MainActivity) activity;
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must be MainActivity");
        }

        mActivity.bindMatchedUpdateCallback(this);

        sensorMan = (SensorManager)activity.getSystemService(Context.SENSOR_SERVICE);
        gyro = sensorMan.getDefaultSensor(Sensor.TYPE_GYROSCOPE);
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mActivity.unbindBeaconsUpdateCallback(this);
        mActivity = null;
    }

    private SensorManager sensorMan;
    private Sensor gyro;

    @Override
    public void onResume() {
        super.onResume();
        sensorMan.registerListener(this, gyro,
                SensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    public void onPause() {
        super.onPause();
        sensorMan.unregisterListener(this);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if (event.sensor.getType() == Sensor.TYPE_GYROSCOPE){
            float[] force = event.values.clone();
            // Shake detection
            float x = force[0];
            float y = force[1];
            float z = force[2];
//            Log.i("Sensors", String.format("x: %.2f y: %.2f z: %.2f", x, y, z));

            onGyroData(x, y, z);
        }

    }

    private LinkedList<Float> cache = new LinkedList<>();
    private int cacheSize = 8;
    private final float magicOpenConstant = 0.4f;

    private boolean closed = true;
    private boolean opening = false;
    private boolean closing = false;
    private int openDirection = 0; // 0: unknown -1: negative opens 1: positive opens

    private void onGyroData(float x, float y, float z) {
        float abs = Math.abs(y);
        while(cache.size() >= cacheSize) {
            cache.removeFirst();
        }
        cache.addLast(abs);

        float avg = 0;
        if(!cache.isEmpty()) {
            for(Float v : cache) {
                avg += v;
            }
            avg /= cache.size();
        }

        if(avg > magicOpenConstant) {
            // first run: determine if positive opens or closes
            if(openDirection == 0 && abs > magicOpenConstant) {
                if(y < 0) {
                    openDirection = -1;
                } else {
                    openDirection = 1;
                }
            }

            // opening or closing
            if(closed) {
                opening = true;
                if(callback != null) {
                    callback.startOpening();
                }
            } else {
                closing = true;
                if(callback != null) {
                    callback.startClosing();
                }
            }
        } else {
            // open or closed if we did something
            if(opening) {
                closed = false;
                opening = false;
                if(callback != null) {
                    callback.opened();
                }
            }
            if(closing) {
                closed = true;
                closing = false;
                if(callback != null) {
                    callback.closed();
                }
            }
        }

        String text = "Last " + cache.size() + ": " + String.format("%.2f", avg) + "\n";
        for(float v : cache) {
            text += String.format("%.2f", v) + "\n";
        }

        String state;
        if(opening || closing) {
            state = opening ? "OPENING" : "CLOSING";
        } else {
            state = closed ? "CLOSED" : "OPEN";
        }

        final String stateCopy = state;
        final String copy = text;
        if(mActivity != null) {
            mActivity.runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    View root = getView();
                    if(root != null) {
                        TextView v = (TextView) root.findViewById(android.R.id.text1);
                        v.setText(copy);
                        TextView vs = (TextView) root.findViewById(R.id.openimg);
                        vs.setText(stateCopy);
                    }
                }
            });
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        // required method
    }

}
