#!/bin/bash

# Function check if an element exist in a string
function _contains_element() {
    for e in "${@:2}"; do [[ $e == $1 ]] && break; done;
}

PS3="Enter option: "

select type_device in "ext3" "ext4" "crypto_LUKS"; do
    if _contains_element "${type_device}" "ext3" "ext4" "crypto_LUKS"; then
    break
    else
      printf "Invalid option \n"
    fi
done

if [[ $type_device == "crypto_LUKS" ]]; then

    devices_list=( $(blkid | grep "crypto_LUKS" | awk '{print $1}' | cut -d":" -f1) )
    if [[ -n $devices_list ]]; then

        select device in "${devices_list[@]}"; do
            if _contains_element "${device}" "${devices_list[@]}"; then
            break
            else
            printf "Invalid option \n"
            fi
        done

    fi    
    
    echo "cryptsetup open ${device} filesystem"


else

    devices_list=( $(blkid | grep "ext" | awk '{print $1}' | cut -d":" -f1) )
    
    for partition in ${devices_list}; do
        sudo mount $partition /mnt
        if [[ -f "/mnt/etc/os-release" ]]; then
            distro_name=$(cat /mnt/etc/os-release | grep ^NAME | cut -d"=" -f2 | cut -d"\"" -f2)
            if [[ "$distro_name" == "Arch Linux" ]] || [[ "$distro_name" == "Manjaro Linux" ]]; then
                printf "$distro_name device found!\n"
                exit 0
            else
                umount /mnt          
            fi
        else
            umount /mnt        
        fi
    done

fi





# if [[ $type_device == "crypto_LUKS" ]]; then
#     echo "cryptsetup open ${device} filesystem"
# fi


# for partition in ${devices_list}; do
#     sudo mount $partition /mnt
#     if [[ -f "/mnt/etc/os-release" ]]; then
#         distro_name=$(cat /mnt/etc/os-release | grep ^NAME | cut -d"=" -f2 | cut -d"\"" -f2)
#         if [[ "$distro_name" == "Arch Linux" ]] || [[ "$distro_name" == "Manjaro Linux" ]]; then
#             printf "$distro_name device found!\n"
#             exit 0
#         else
#             umount /mnt          
#         fi
#     else
#         umount /mnt        
#     fi
# done

    # qtdpartitions=( $(lsblk -f | grep ext | cut -d"e" -f1 | cut -d"a" -f2 | sed ':a;$!N;s/\n//;ta;'n) )
    # qtdpartitions_refactored="$(expr ${#qtdpartitions[@]} - 1)"
    # echo "$qtdpartitions"
    # echo "$qtdpartitions_refactored"
    # for (( x = 0; x < ${#qtdpartitions[@]}; x++ )); do
    #   if [[ $x == $qtdpartitions_refactored ]] && [[ ! -f "/mnt/etc/os-release" ]]; then
    #     printf "${Error} ${White} Sorry, but it seems that the mounted partitions did not return the file: \"${mount_dir}/etc/os-release\" :(\n${None}"
    #     exit 1
    #   fi
    # done