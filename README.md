## LiveOSC2

This repository contains code of LiveOSC2 extended to work in conjunction with
[oscremap](https://github.com/mwicat/oscremap) tool.

## Communication

- Listens on address: `127.0.0.1:9001`
- Sends to address: `127.0.0.1:9000`

## Testing

Receive messages from DAW:

```bash
oscli dump -P 9000
```

Send messages to DAW:

```bash
oscli send -P 9001 
```


## Installation

### MacOS

```bash
./install_osx.sh
```

## Messages

### Receives messages

- `/fx/param/[PARAM_POS]/val` - set FX parameter value at position `PARAM_POS`

### Sends messages

- `/fx/param/[PARAM_POS]/val` - FX parameter value at position `PARAM_POS`
- `/fx/param/[PARAM_POS]/name` - name of FX parameter at position `PARAM_POS`
- `/fx/param/[PARAM_POS]/str` - string representation of FX parameter value at position `PARAM_POS`
- `/fx/name [NAME]` - name of current FX
