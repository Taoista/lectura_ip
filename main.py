from pythonping import ping


def main():
    print("iniciando el software")

    
    ip_movistar = "200.54.31.66"
    ip_netline = "200.71.193.54"
    ip_vtr = "no ip"


    print("inciando el software para el testing")


    # print(f"este es la ip de movistar => {ip_movistar}")
    # print(f"esta es la ip de netline => {ip_netline}")
    # print(f"esta es la ip de VTR => {ip_vtr}")


    
    print(ping(ip_netline))

    print("------- terminndo el software de testeo-----------------")


# movistart: 200.54.31.66
# netline: 200.71.193.54
# vtr: no la tengo


if __name__ == "__main__":
    main()