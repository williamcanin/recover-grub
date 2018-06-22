#!/bin/bash

PS3="Enter option: "

# Function check if an element exist in a string
function _contains_element() {
    for e in "${@:2}"; do [[ $e == $1 ]] && break; done;
}

# Function to select the partition type. 
function _select_type_partition(){
    select type_device in "ext" "crypto_LUKS"; do
        if _contains_element "${type_device}" "ext" "crypto_LUKS"; then
        break
        else
        printf "Invalid option \n"
        fi
    done
}

# Function to select encrypted partitions (crypto_LUKS).
function _select_mount_partition_crypto(){
    devices_list=( $(blkid | grep "$1" | awk '{print $1}' | cut -d":" -f1) )
    if [[ -n $devices_list ]]; then
        select device in "${devices_list[@]}"; do
            if _contains_element "${device}" "${devices_list[@]}"; then
                
                # Open partition crypted
                echo "cryptsetup open ${device} $3"
                # Mount partition crypted
                echo "mount /dev/mapper/$3 $2"
                break
            else
                printf "Invalid option\n"
            fi
        done
        

        
    fi    
}

# Function to mount partitions of type EXT recursively.
function _select_mount_partition_ext(){
    devices_list=( $(blkid | grep "$1" | awk '{print $1}' | cut -d":" -f1) )
    
    for partition in ${devices_list}; do
        sudo mount $partition $2
        if [[ -f "$2/etc/os-release" ]]; then
            distro_name=$(cat $2/etc/os-release | grep ^NAME | cut -d"=" -f2 | cut -d"\"" -f2)
            if [[ "$distro_name" == "Arch Linux" ]] || [[ "$distro_name" == "Manjaro Linux" ]]; then
                printf "$distro_name device found!\n"
                exit 0
            else
                umount $2          
            fi
        else
            umount $2       
        fi
    done
}

_select_type_partition
if [[ $type_device == "crypto_LUKS" ]]; then
    _select_mount_partition_crypto "crypto_LUKS" "/mnt" "filesystem"
else
    _select_mount_partition_ext "ext" "/mnt"
fi

