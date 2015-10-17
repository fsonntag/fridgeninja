package ninja.fridge.fridgeninja;

import org.altbeacon.beacon.Beacon;

import java.util.Collection;

/**
 * Created by Benedikt on 17.10.2015.
 */
public interface BeaconsUpdateCallback {
    public void beaconsChanged(Collection<Beacon> newBeacons);
}

